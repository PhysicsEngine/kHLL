__author__ = 'lewuathe'

from sklearn import datasets
from sklearn.cluster import KMeans

def main():
    iris = datasets.load_iris()

    X = iris.data  # we only take the first two features.
    Y = iris.target

    model = KMeans(n_clusters=8,
                   init='k-means++',
                   n_init=10,
                   max_iter=300,
                   tol=0.0001,
                   precompute_distances=True,
                   verbose=0,
                   random_state=None,
                   copy_x=True,
                   n_jobs=1)
    model.fit(X)

    print(model.labels_)


if __name__ == "__main__":
    main()
