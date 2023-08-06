# -*- coding: utf-8 -*-
from __future__ import print_function, division
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor, ExtraTreesRegressor, ExtraTreesClassifier
from sklearn.tree._tree import DTYPE, DOUBLE
from sklearn.utils import check_random_state
from sklearn.utils.validation import _check_sample_weight
from sklearn.utils.multiclass import check_classification_targets, type_of_target
from sklearn.ensemble._forest import  _get_n_samples_bootstrap
from sklearn.exceptions import DataConversionWarning
from joblib import Parallel, delayed
from warnings import catch_warnings, simplefilter, warn
from scipy.sparse import issparse
import numpy as np
import pandas as pd


# =====
# Utility
# =====
# !!! This section has been added to handle Pandas
def _check_pandas(X, y, sample_weight, bootstrap_weight):
    obj_is_pandas = {
        "X":isinstance(X,pd.DataFrame),
        "y":isinstance(y,pd.Series),
        "sample_weight":isinstance(sample_weight,pd.Series),
        "bootstrap_weight":isinstance(bootstrap_weight,pd.Series),
    }
    
    index = None
    columns = None
    
    if obj_is_pandas["y"]:
        assert obj_is_pandas["X"], \
            "If`y` is a pd.Series the `X` must be a pd.DataFrame with the same index as `y`"
    
    if obj_is_pandas["sample_weight"]:
        assert obj_is_pandas["X"], \
            "If`sample_weight` is a pd.Series the `X` must be a pd.DataFrame with the same index as `sample_weight`"
        
    if obj_is_pandas["bootstrap_weight"]:
        assert obj_is_pandas["X"], \
            "If`bootstrap_weight` is a pd.Series the `X` must be a pd.DataFrame with the same index as `bootstrap_weight`"
        
    # X is pandas
    if obj_is_pandas["X"]:
        index = X.index
        columns = X.columns
        
        # y
        assert obj_is_pandas["y"], \
            "If `X` is a pd.DataFrame then `y` must be a pd.Series with the same index as `X`"
        assert np.all(X.index == y.index), \
            "If `X` is a pd.DataFrame then `y` must be a pd.Series with the same index as `X`"
        # sample_weight
        assert any([obj_is_pandas["sample_weight"], sample_weight is None]), \
            "If `X` or `y` are pandas objects then `sample_weight` must be `NoneType` or a pd.Series with the same index as `X`"
        if obj_is_pandas["sample_weight"]:
            assert np.all(X.index == sample_weight.index), \
                "If `X` or `y` are pandas objects then `sample_weight` must be `NoneType` or a pd.Series with the same index as `X`"
            sample_weight = sample_weight.values
            
        # bootstrap_weight
        assert any([obj_is_pandas["bootstrap_weight"], bootstrap_weight is None]), \
            "If `X` or `y` are pandas objects then `bootstrap_weight` must be `NoneType` or a pd.Series with the same index as `X`"
        if obj_is_pandas["bootstrap_weight"]:
            assert np.all(X.index == bootstrap_weight.index), \
                "If `X` or `y` are pandas objects then `bootstrap_weight` must be `NoneType` or a pd.Series with the same index as `X`"
            bootstrap_weight = bootstrap_weight.values
            
        X = X.values
        y = y.values
    return (X, y, sample_weight, bootstrap_weight, index, columns)
    
    
def _generate_sample_indices_weighted_bootstrap(random_state, n_samples, n_samples_bootstrap, bootstrap_weight):
    """
    The version of sklearn.ensemble._forest._generate_sample_indices()
    with an extra parameter `bootstrap_weight`
    Private function used to _parallel_build_trees_weighted_bootstrap function."""
    
    if bootstrap_weight is None:
        p = np.ones(n_samples, dtype=float)
    else:
        p = np.array(bootstrap_weight, dtype=float)
    p = p
    p /= p.sum()

    random_instance = check_random_state(random_state)

    # !!! This section has been modified to handle weighted bootstrapping
    # -------------------------------------------------------------------
    sample_indices = random_instance.choice(np.arange(n_samples), n_samples_bootstrap, True, p)
    # -------------------------------------------------------------------

    return sample_indices

def _parallel_build_trees_weighted_bootstrap(
    tree,
    bootstrap,
    X,
    y,
    sample_weight,
    bootstrap_weight,
    tree_idx,
    n_trees,
    verbose=0,
    class_weight=None,
    n_samples_bootstrap=None,
):
    """
    The version of sklearn.ensemble._forest._parallel_build_trees()
    with an extra parameter `bootstrap_weight`
    Private function used to fit a single tree in parallel."""
    if verbose > 1:
        print("building tree %d of %d" % (tree_idx + 1, n_trees))

    if bootstrap:
        n_samples = X.shape[0]
        if sample_weight is None:
            curr_sample_weight = np.ones((n_samples,), dtype=np.float64)
        else:
            curr_sample_weight = sample_weight.copy()

        # !!! This section has been modified to handle weighted bootstrapping
        # -------------------------------------------------------------------
        indices = _generate_sample_indices_weighted_bootstrap( 
            tree.random_state, n_samples, n_samples_bootstrap, bootstrap_weight
        )
        # -------------------------------------------------------------------
        sample_counts = np.bincount(indices, minlength=n_samples)
        curr_sample_weight *= sample_counts

        if class_weight == "subsample":
            with catch_warnings():
                simplefilter("ignore", DeprecationWarning)
                curr_sample_weight *= compute_sample_weight("auto", y, indices=indices)
        elif class_weight == "balanced_subsample":
            curr_sample_weight *= compute_sample_weight("balanced", y, indices=indices)

        tree.fit(X, y, sample_weight=curr_sample_weight, check_input=False)
    else:
        tree.fit(X, y, sample_weight=sample_weight, check_input=False)

    return tree

# WeightedBootstrapRandomForestClassifier
class WeightedBootstrapRandomForestClassifier(RandomForestClassifier):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def fit(self, X, y, sample_weight=None, bootstrap_weight=None):
        """
        A version of sklearn.ensemble.BaseForest.fit() method
        with extra parameter `bootstrap_weight` which defines the
        probablity that a sample will be selected during bootstrapping. 
        
        -------------------------------------------------------
         Implementation adapted from the following sources:
             * Credits to @boris-silantev
             https://stackoverflow.com/a/73849201/678572
        -------------------------------------------------------

        Build a forest of trees from the training set (X, y) with sampling
        determined by `bootstrap_weight`
        
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The training input samples. Internally, its dtype will be converted
            to ``dtype=np.float32``. If a sparse matrix is provided, it will be
            converted into a sparse ``csc_matrix``.
        y : array-like of shape (n_samples,) or (n_samples, n_outputs)
            The target values (class labels in classification, real numbers in
            regression).
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted. Splits
            that would create child nodes with net zero or negative weight are
            ignored while searching for a split in each node. In the case of
            classification, splits are also ignored if they would result in any
            single class carrying a negative weight in either child node.
        bootstrap_weight : array-like of shape (n_samples,), default=None
            Sample-wise weights. If None, then samples are equally weighted.
            The weights determine the probability that the sample will be selected
            while bootstrapping.
        Returns
        -------
        self : object
            Fitted estimator.
        """
        # !!! This section has been modified to handle Pandas objects
        # -------------------------------------------------------------------
        # Check pandas objects
        X, y, sample_weight, bootstrap_weight, index, columns = _check_pandas(X, y, sample_weight, bootstrap_weight)
        # -------------------------------------------------------------------

        # Validate or convert input data
        if issparse(y):
            raise ValueError("sparse multilabel-indicator for y is not supported.")
        if sample_weight is not None:
            sample_weight = _check_sample_weight(sample_weight, X)

        if issparse(X):
            # Pre-sort indices to avoid that each individual tree of the
            # ensemble sorts the indices.
            X.sort_indices()

        y = np.atleast_1d(y)
        if y.ndim == 2 and y.shape[1] == 1:
            warn(
                "A column-vector y was passed when a 1d array was"
                " expected. Please change the shape of y to "
                "(n_samples,), for example using ravel().",
                DataConversionWarning,
                stacklevel=2,
            )

        if y.ndim == 1:
            # reshape is necessary to preserve the data contiguity against vs
            # [:, np.newaxis] that does not.
            y = np.reshape(y, (-1, 1))

        if self.criterion == "poisson":
            if np.any(y < 0):
                raise ValueError(
                    "Some value(s) of y are negative which is "
                    "not allowed for Poisson regression."
                )
            if np.sum(y) <= 0:
                raise ValueError(
                    "Sum of y is not strictly positive which "
                    "is necessary for Poisson regression."
                )

        self.n_outputs_ = y.shape[1]

        y, expanded_class_weight = self._validate_y_class_weight(y)

        if getattr(y, "dtype", None) != DOUBLE or not y.flags.contiguous:
            y = np.ascontiguousarray(y, dtype=DOUBLE)

        if expanded_class_weight is not None:
            if sample_weight is not None:
                sample_weight = sample_weight * expanded_class_weight
            else:
                sample_weight = expanded_class_weight

        if not self.bootstrap and self.max_samples is not None:
            raise ValueError(
                "`max_sample` cannot be set if `bootstrap=False`. "
                "Either switch to `bootstrap=True` or set "
                "`max_sample=None`."
            )
        elif self.bootstrap:
            n_samples_bootstrap = _get_n_samples_bootstrap(
                n_samples=X.shape[0], max_samples=self.max_samples
            )
        else:
            n_samples_bootstrap = None

        self._validate_estimator()
        if isinstance(self, (RandomForestRegressor)):
            # TODO(1.3): Remove "auto"
            if self.max_features == "auto":
                warn(
                    "`max_features='auto'` has been deprecated in 1.1 "
                    "and will be removed in 1.3. To keep the past behaviour, "
                    "explicitly set `max_features=1.0` or remove this "
                    "parameter as it is also the default value for "
                    "RandomForestRegressors and ExtraTreesRegressors.",
                    FutureWarning,
                )
        elif isinstance(self, (RandomForestClassifier)):
            # TODO(1.3): Remove "auto"
            if self.max_features == "auto":
                warn(
                    "`max_features='auto'` has been deprecated in 1.1 "
                    "and will be removed in 1.3. To keep the past behaviour, "
                    "explicitly set `max_features='sqrt'` or remove this "
                    "parameter as it is also the default value for "
                    "RandomForestClassifiers and ExtraTreesClassifiers.",
                    FutureWarning,
                )

        if not self.bootstrap and self.oob_score:
            raise ValueError("Out of bag estimation only available if bootstrap=True")

        random_state = check_random_state(self.random_state)

        if not self.warm_start or not hasattr(self, "estimators_"):
            # Free allocated memory, if any
            self.estimators_ = []

        n_more_estimators = self.n_estimators - len(self.estimators_)

        if n_more_estimators < 0:
            raise ValueError(
                "n_estimators=%d must be larger or equal to "
                "len(estimators_)=%d when warm_start==True"
                % (self.n_estimators, len(self.estimators_))
            )

        elif n_more_estimators == 0:
            warn(
                "Warm-start fitting without increasing n_estimators does not "
                "fit new trees."
            )
        else:
            if self.warm_start and len(self.estimators_) > 0:
                # We draw from the random state to get the random state we
                # would have got if we hadn't used a warm_start.
                random_state.randint(MAX_INT, size=len(self.estimators_))

            trees = [
                self._make_estimator(append=False, random_state=random_state)
                for i in range(n_more_estimators)
            ]

            # Parallel loop: we prefer the threading backend as the Cython code
            # for fitting the trees is internally releasing the Python GIL
            # making threading more efficient than multiprocessing in
            # that case. However, for joblib 0.12+ we respect any
            # parallel_backend contexts set at a higher level,
            # since correctness does not rely on using threads.
            trees = Parallel(
                n_jobs=self.n_jobs,
                verbose=self.verbose,
                prefer="threads",
            )(
                # !!! This section has been modified to handle weighted bootstrapping
                # -------------------------------------------------------------------
                delayed(_parallel_build_trees_weighted_bootstrap)( 
                    t,
                    self.bootstrap,
                    X,
                    y,
                    sample_weight,
                    bootstrap_weight,
                    i,
                    len(trees),
                    verbose=self.verbose,
                    class_weight=self.class_weight,
                    n_samples_bootstrap=n_samples_bootstrap,
                # -------------------------------------------------------------------

                )
                for i, t in enumerate(trees)
            )

            # Collect newly grown trees
            self.estimators_.extend(trees)

        if self.oob_score:
            y_type = type_of_target(y)
            if y_type in ("multiclass-multioutput", "unknown"):
                # FIXME: we could consider to support multiclass-multioutput if
                # we introduce or reuse a constructor parameter (e.g.
                # oob_score) allowing our user to pass a callable defining the
                # scoring strategy on OOB sample.
                raise ValueError(
                    "The type of target cannot be used to compute OOB "
                    f"estimates. Got {y_type} while only the following are "
                    "supported: continuous, continuous-multioutput, binary, "
                    "multiclass, multilabel-indicator."
                )
            self._set_oob_score_and_attributes(X, y)

        # Decapsulate classes_ attributes
        if hasattr(self, "classes_") and self.n_outputs_ == 1:
            self.n_classes_ = self.n_classes_[0]
            self.classes_ = self.classes_[0]

        # !!! This section has been modified to handle Pandas objects
        # -------------------------------------------------------------------
        self.sample_names_in_ = np.asarray(index)
        self.feature_names_in_ = np.asarray(columns)
        if bootstrap_weight is not None:
            self.bootstrap_weight_ = bootstrap_weight.copy()
        # -------------------------------------------------------------------
        
        return self
    
# WeightedBootstrapRandomForestRegressor
class WeightedBootstrapRandomForestRegressor(RandomForestRegressor):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def fit(self, X, y, sample_weight=None, bootstrap_weight=None):
        """
        A version of sklearn.ensemble.BaseForest.fit() method
        with extra parameter `bootstrap_weight` which defines the
        probablity that a sample will be selected during bootstrapping. 
        
        -------------------------------------------------------
         Implementation adapted from the following sources:
             * Credits to @boris-silantev
             https://stackoverflow.com/a/73849201/678572
        -------------------------------------------------------

        Build a forest of trees from the training set (X, y) with sampling
        determined by `bootstrap_weight`
        
        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The training input samples. Internally, its dtype will be converted
            to ``dtype=np.float32``. If a sparse matrix is provided, it will be
            converted into a sparse ``csc_matrix``.
        y : array-like of shape (n_samples,) or (n_samples, n_outputs)
            The target values (class labels in classification, real numbers in
            regression).
        sample_weight : array-like of shape (n_samples,), default=None
            Sample weights. If None, then samples are equally weighted. Splits
            that would create child nodes with net zero or negative weight are
            ignored while searching for a split in each node. In the case of
            classification, splits are also ignored if they would result in any
            single class carrying a negative weight in either child node.
        bootstrap_weight : array-like of shape (n_samples,), default=None
            Sample-wise weights. If None, then samples are equally weighted.
            The weights determine the probability that the sample will be selected
            while bootstrapping.
        Returns
        -------
        self : object
            Fitted estimator.
        """
        
        # !!! This section has been modified to handle Pandas objects
        # -------------------------------------------------------------------
        # Check pandas objects
        X, y, sample_weight, bootstrap_weight, index, columns = _check_pandas(X, y, sample_weight, bootstrap_weight)
        # -------------------------------------------------------------------

        # Validate or convert input data
        if issparse(y):
            raise ValueError("sparse multilabel-indicator for y is not supported.")
        X, y = self._validate_data(
            X, y, multi_output=True, accept_sparse="csc", dtype=DTYPE
        )
        if sample_weight is not None:
            sample_weight = _check_sample_weight(sample_weight, X)

        if issparse(X):
            # Pre-sort indices to avoid that each individual tree of the
            # ensemble sorts the indices.
            X.sort_indices()

        y = np.atleast_1d(y)
        if y.ndim == 2 and y.shape[1] == 1:
            warn(
                "A column-vector y was passed when a 1d array was"
                " expected. Please change the shape of y to "
                "(n_samples,), for example using ravel().",
                DataConversionWarning,
                stacklevel=2,
            )

        if y.ndim == 1:
            # reshape is necessary to preserve the data contiguity against vs
            # [:, np.newaxis] that does not.
            y = np.reshape(y, (-1, 1))

        if self.criterion == "poisson":
            if np.any(y < 0):
                raise ValueError(
                    "Some value(s) of y are negative which is "
                    "not allowed for Poisson regression."
                )
            if np.sum(y) <= 0:
                raise ValueError(
                    "Sum of y is not strictly positive which "
                    "is necessary for Poisson regression."
                )

        self.n_outputs_ = y.shape[1]

        y, expanded_class_weight = self._validate_y_class_weight(y)

        if getattr(y, "dtype", None) != DOUBLE or not y.flags.contiguous:
            y = np.ascontiguousarray(y, dtype=DOUBLE)

        if expanded_class_weight is not None:
            if sample_weight is not None:
                sample_weight = sample_weight * expanded_class_weight
            else:
                sample_weight = expanded_class_weight

        if not self.bootstrap and self.max_samples is not None:
            raise ValueError(
                "`max_sample` cannot be set if `bootstrap=False`. "
                "Either switch to `bootstrap=True` or set "
                "`max_sample=None`."
            )
        elif self.bootstrap:
            n_samples_bootstrap = _get_n_samples_bootstrap(
                n_samples=X.shape[0], max_samples=self.max_samples
            )
        else:
            n_samples_bootstrap = None

        # Check parameters
        self._validate_estimator()
        # TODO(1.2): Remove "mse" and "mae"
        if isinstance(self, (RandomForestRegressor, ExtraTreesRegressor)):
            if self.criterion == "mse":
                warn(
                    "Criterion 'mse' was deprecated in v1.0 and will be "
                    "removed in version 1.2. Use `criterion='squared_error'` "
                    "which is equivalent.",
                    FutureWarning,
                )
            elif self.criterion == "mae":
                warn(
                    "Criterion 'mae' was deprecated in v1.0 and will be "
                    "removed in version 1.2. Use `criterion='absolute_error'` "
                    "which is equivalent.",
                    FutureWarning,
                )

            # TODO(1.3): Remove "auto"
            if self.max_features == "auto":
                warn(
                    "`max_features='auto'` has been deprecated in 1.1 "
                    "and will be removed in 1.3. To keep the past behaviour, "
                    "explicitly set `max_features=1.0` or remove this "
                    "parameter as it is also the default value for "
                    "RandomForestRegressors and ExtraTreesRegressors.",
                    FutureWarning,
                )
        elif isinstance(self, (RandomForestClassifier, ExtraTreesClassifier)):
            # TODO(1.3): Remove "auto"
            if self.max_features == "auto":
                warn(
                    "`max_features='auto'` has been deprecated in 1.1 "
                    "and will be removed in 1.3. To keep the past behaviour, "
                    "explicitly set `max_features='sqrt'` or remove this "
                    "parameter as it is also the default value for "
                    "RandomForestClassifiers and ExtraTreesClassifiers.",
                    FutureWarning,
                )

        if not self.bootstrap and self.oob_score:
            raise ValueError("Out of bag estimation only available if bootstrap=True")

        random_state = check_random_state(self.random_state)

        if not self.warm_start or not hasattr(self, "estimators_"):
            # Free allocated memory, if any
            self.estimators_ = []

        n_more_estimators = self.n_estimators - len(self.estimators_)

        if n_more_estimators < 0:
            raise ValueError(
                "n_estimators=%d must be larger or equal to "
                "len(estimators_)=%d when warm_start==True"
                % (self.n_estimators, len(self.estimators_))
            )

        elif n_more_estimators == 0:
            warn(
                "Warm-start fitting without increasing n_estimators does not "
                "fit new trees."
            )
        else:
            if self.warm_start and len(self.estimators_) > 0:
                # We draw from the random state to get the random state we
                # would have got if we hadn't used a warm_start.
                random_state.randint(MAX_INT, size=len(self.estimators_))

            trees = [
                self._make_estimator(append=False, random_state=random_state)
                for i in range(n_more_estimators)
            ]

            # Parallel loop: we prefer the threading backend as the Cython code
            # for fitting the trees is internally releasing the Python GIL
            # making threading more efficient than multiprocessing in
            # that case. However, for joblib 0.12+ we respect any
            # parallel_backend contexts set at a higher level,
            # since correctness does not rely on using threads.
            trees = Parallel(
                n_jobs=self.n_jobs,
                verbose=self.verbose,
                prefer="threads",
            )(      
                # !!! This section has been modified to handle weighted bootstrapping
                # -------------------------------------------------------------------
                delayed(_parallel_build_trees_weighted_bootstrap)( 
                    t,
                    self.bootstrap,
                    X,
                    y,
                    sample_weight,
                    bootstrap_weight,
                    i,
                    len(trees),
                    verbose=self.verbose,
                    class_weight=self.class_weight,
                    n_samples_bootstrap=n_samples_bootstrap,
                # -------------------------------------------------------------------
                )
                for i, t in enumerate(trees)
            )

            # Collect newly grown trees
            self.estimators_.extend(trees)

        if self.oob_score:
            y_type = type_of_target(y)
            if y_type in ("multiclass-multioutput", "unknown"):
                # FIXME: we could consider to support multiclass-multioutput if
                # we introduce or reuse a constructor parameter (e.g.
                # oob_score) allowing our user to pass a callable defining the
                # scoring strategy on OOB sample.
                raise ValueError(
                    "The type of target cannot be used to compute OOB "
                    f"estimates. Got {y_type} while only the following are "
                    "supported: continuous, continuous-multioutput, binary, "
                    "multiclass, multilabel-indicator."
                )
            self._set_oob_score_and_attributes(X, y)

        # Decapsulate classes_ attributes
        if hasattr(self, "classes_") and self.n_outputs_ == 1:
            self.n_classes_ = self.n_classes_[0]
            self.classes_ = self.classes_[0]

        # !!! This section has been modified to handle Pandas objects
        # -------------------------------------------------------------------
        self.sample_names_in_ = np.asarray(index)
        self.feature_names_in_ = np.asarray(columns)
        if bootstrap_weight is not None:
            self.bootstrap_weight_ = bootstrap_weight.copy()
        # -------------------------------------------------------------------

        return self