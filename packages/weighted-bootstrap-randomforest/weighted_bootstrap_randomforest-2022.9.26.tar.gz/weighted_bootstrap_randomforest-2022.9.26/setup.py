from setuptools import setup

# Version
version = None
with open("weighted_bootstrap_randomforest/__init__.py", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith("__version__"):
            version = line.split("=")[-1].strip().strip('"')
assert version is not None, "Check version in weighted_bootstrap_randomforest/__init__.py"

setup(
name='weighted_bootstrap_randomforest',
    version=version,
    description='Implementations of Weighted bootstrap Random Forests classifier and regressors',
    url='https://github.com/jolespin/weighted_bootstrap_randomforest',
    author='Josh L. Espinoza',
    author_email='jespinoz@jcvi.org',
    license='BSD-3',
    packages=["weighted_bootstrap_randomforest"],
    install_requires=[
        "pandas >= 0.24.2",
        "numpy >= 1.11",
        "joblib",
        "scikit-learn >= 0.24.2",
      ],
)
