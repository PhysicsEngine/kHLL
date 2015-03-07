from sklearn import datasets
from kHLL.hash.image import md5_for_vec
from kHLL.kestimate import GaussianWeightedKEstimator

def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target
    
    model = GaussianWeightedKEstimator(1, 5, md5_for_vec, 20)
    model.train(X)

    print(model.getK())

if __name__ == "__main__":
    main()
