__author__ = 'lewuathe'

from sklearn import datasets

from kHLL.hash.image import md5_for_vec
from kHLL.HLL.hyperloglog import BaseHyperLogLog

def main():
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    for i in xrange(1, 20):
        model = BaseHyperLogLog(0.01, i, md5_for_vec)
        for x in X:
            model.update(x)

        #print(len(Y))
        print(model.calc_cardinality())


if __name__ == "__main__":
    main()
