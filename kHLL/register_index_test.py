__author__ = 'lewuathe'

from kestimate import BaseKEstimater
from HLL.hyperloglog import BaseHyperLogLog
from hash.image import md5_for_vec
from multiprocessing import Process, Queue

class RIKEstimator(BaseKEstimater):
    """
    K estimator by trimming parallel HLL estimation
    """
    IS_PARALLEL = False
    MAX_REGISTER_INDEX = 20

    @classmethod
    def delegate(cls, q, constant, register_index, data, hash_func):
        hll = BaseHyperLogLog(constant, register_index, hash_func)
        for d in data:
            hll.update(d)
        q.put((hll.calc_cardinality(), register_index))

    def train(self, data):
        if RIKEstimator.IS_PARALLEL:
            self.parallel_train(data)
        else:
            self.serial_train(data)

    def serial_train(self, data):
        """
        Serial traingin on each HLL estimation
        :param data:
        :return:
        """
        results = []
        for i in xrange(1, RIKEstimator.MAX_REGISTER_INDEX):
            hll = BaseHyperLogLog(0.01, i, md5_for_vec)
            for d in data:
                hll.update(d)
            if i < RIKEstimator.MAX_REGISTER_INDEX / 2:
                results.append(hll.calc_cardinality())
        self.k = reduce(lambda x, y: x + y, results) / len(results)

    def parallel_train(self, data):
        """
        Parallel training on each HLL estimation
        :param data:
        :return:
        """
        jobs = []
        q = Queue()
        for i in xrange(1, RIKEstimator.MAX_REGISTER_INDEX):
            jobs.append(Process(target = RIKEstimator.delegate,
                        args = (q, 0.01, i, data, md5_for_vec)))

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

        results = []
        while not q.empty():
            ret = q.get()
            if ret[1] < RIKEstimator.MAX_REGISTER_INDEX / 2:
                results.append(ret[0])

        self.k = reduce(lambda x, y: x + y, results) / len(results)


if __name__ == "__main__":
    from sklearn import datasets
    estimator = RIKEstimator(5, 1, md5_for_vec)
    X = datasets.load_iris()
    estimator.train(X.data)
    print(estimator.getK())
