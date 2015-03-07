__author__ = 'lewuathe'

from sklearn import datasets

from hash.image import md5_for_vec
from HLL.hyperloglog import BaseHyperLogLog

def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    model = BaseHyperLogLog(0.01, 5, md5_for_vec)
    for x in X:
        model.update(x)

    print(len(Y))
    print(model.cals_cardinality())



if __name__ == "__main__":
    main()
