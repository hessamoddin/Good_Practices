# Generate synthetic data
# Randomly generates synthetic data and scatter plots 
N_CLASSES = 4
X, y = sklearn.datasets.make_classification(
    n_features=2, n_redundant=0,
    n_classes=N_CLASSES, n_clusters_per_class=1)
# Convert to theano floatX
X = X.astype(theano.config.floatX)
# Labels should be ints
y = y.astype('int32')
# Make a scatter plot where color encodes class
plt.scatter(X[:, 0], X[:, 1], c=y)
