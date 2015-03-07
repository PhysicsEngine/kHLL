__author__ = 'lewuathe'


from sklearn import datasets
from sklearn.cluster import KMeans

from kHLL.hash.image import md5_for_vec
from kHLL.kestimate import HyperKEstimator

def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    model = HyperKEstimator(1, 5, md5_for_vec, 20)
    model.train(X)

    kmeans_model = KMeans(n_clusters=model.getK(),
                   init='k-means++',
                   n_init=10,
                   max_iter=300,
                   tol=0.0001,
                   precompute_distances=True,
                   verbose=0,
                   random_state=None,
                   copy_x=True,
                   n_jobs=1)

    kmeans_model.fit(X)
    print(kmeans_model.labels_)

if __name__ == "__main__":
    main()

