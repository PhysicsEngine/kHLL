__author__ = 'lewuathe'

from sklearn import datasets
from sklearn.mixture import DPGMM

def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    model = DPGMM()

    model.fit(X)
    print(model.n_components)


if __name__ == "__main__":
    main()
