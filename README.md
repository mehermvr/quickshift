# Quickshit++ (Modified)

This is a modified version of the original [quickshit repository](https://github.com/google/quickshift) with the changes basically being to make it a pybind package instead of a cython one.
Additionally, the C++ core library code has been modified (i.e., I tried to clean it up to whatever extent I could but failed).

Installation should be a simple

```bash
pip install git+https://github.com/mehermvr/quickshift.git
pip install -e ".[test]"
```

In case the above doesn't work, check if you might need `--no-build-isolation` in case of conflicts with your cmake install

```bash
pip install --no-build-isolation -v .
pip install --no-build-isolation -v git+https://github.com/mehermvr/quickshift.git
```

There are some unit tests to ensure parity with the original implementation.

```bash
pytest tests
```

# Original README below

# Quickshift++

This is not an officially supported Google product

Density-based clustering algorithm based on mode-seeking.

# Usage

**Initializiation**:

```python
QuickshiftPP(k, beta)
```

k: number of neighbors in k-NN

beta: fluctuation parameter which ranges between 0 and 1.

**Finding Clusters**:

```python
fit(X)
```

X is the data matrix, where each row is a datapoint in euclidean space.

fit performs the clustering. The final result can be found in QuickshiftPP.memberships.

**Example** (mixture of two gaussians):

```python
from QuickshiftPP import \*
import numpy as np

X = [np.random.normal(0, 1, 2) for i in range(100)] + [np.random.normal(5, 1, 2) for i in range(100)]
y = [0] _ 100 + [1] _ 100

# Declare a Quickshift++ model with tuning hyperparameters.

model = QuickshiftPP(k=20, beta=.5)

# Compute the clustering.

model.fit(X)
y_hat = model.memberships

from sklearn.metrics.cluster import adjusted_rand_score, adjusted_mutual_info_score
print("Adj. Rand Index Score: %f." % adjusted_rand_score(y_hat, y))
print("Adj. Mutual Info Score: %f." % adjusted_mutual_info_score(y_hat, y))
```

# Install

This package uses distutils, which is the default way of installing
python modules.

To install for all users on Unix/Linux::

```bash
sudo python setup.py build; python setup.py install
```

# Dependencies

python 2.7, scikit-learn
