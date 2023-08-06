## Weighted Boostrap Random Forests

Implementations for weighted bootstrap random forest classifier and regressor models.

### Usage: 

**Classification:**

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from weighted_bootstrap_randomforest import WeightedBootstrapRandomForestClassifier, WeightedBootstrapRandomForestRegressor

# Load data
X = pd.read_csv("https://github.com/jolespin/walkthroughs/blob/main/data/iris/X.tsv.gz?raw=true", sep="\t", index_col=0, compression="gzip")
y = pd.read_csv("https://github.com/jolespin/walkthroughs/blob/main/data/iris/y.tsv.gz?raw=true", sep="\t", index_col=0, compression="gzip").squeeze()
class_colors = {'setosa': '#db5f57', 'versicolor': '#57db5f', 'virginica': '#5f57db'}
colors = y.map(lambda x: class_colors[x])

# Split data
X_tr, X_te, y_tr, y_te = train_test_split(X,y, random_state=0)

# Classification model
model = WeightedBootstrapRandomForestClassifier(n_estimators=10, random_state=0)

# Unmodified random forest bootstrapping
model.fit(X_tr, y_tr, bootstrap_weight=None)
np.mean(model.predict(X_te) == y_te)
# 0.8947368421052632

# Weighted random forest bootstrapping
bootstrap_weight = y_tr.map(lambda x: {"setosa":1, "versicolor":50, "virginica":49}[x])
model.fit(X_tr, y_tr, bootstrap_weight=bootstrap_weight)
np.mean(model.predict(X_te) == y_te)
# 0.7894736842105263 Yes, it should be lower here because setosa is being largely ignored

```

#### Regression:

```python
# Load data
X = pd.read_csv("https://github.com/jolespin/walkthroughs/blob/main/data/iris/X.tsv.gz?raw=true", sep="\t", index_col=0, compression="gzip")
y = X.iloc[:,-1]
X = X.iloc[:,:-1]

# Split data
X_tr, X_te, y_tr, y_te = train_test_split(X,y, random_state=0)

# Regression model
model = WeightedBootstrapRandomForestRegressor(n_estimators=10, random_state=0)

# Unmodified random forest bootstrapping
model.fit(X_tr, y_tr, bootstrap_weight=None)
np.mean((model.predict(X_te) - y_te)**2)
# 0.08443242977645578

# Use the bootstrap weights from before
model.fit(X_tr, y_tr, bootstrap_weight=bootstrap_weight)
np.mean((model.predict(X_te) - y_te)**2)
# 0.1797231030934477 Yes, it should be worse here because setosa is being largely ignored
```

