from abc import abstractmethod
import numpy
from scipy.stats import norm
from HLL.hyperloglog import BaseHyperLogLog
from hash.image import md5_for_vec
from multiprocessing import Process, Queue

class BaseKEstimater(object):
    def __init__(self, kmin, kmax, hashFunc):
        self.kmin = kmin
        self.kmax = kmax
        self.hashFunc = hashFunc
        self.k = 0
    
    def getK(self):
        if self.k <= 0:
            raise Exception("train failed")

        return int(self.k)

    @abstractmethod
    def train(self, data):
        pass

class CalcWeightLib(object):
    @classmethod
    def gaussian_pdf(cls, value, mean):
        return norm.pdf(value, mean)

class GaussianWeightedKEstimator(BaseKEstimater):
    def __init__(self, kmin, kmax, hashFunc, iter_n):
       BaseKEstimater.__init__(self, kmin, kmax, hashFunc)
       self.mean = numpy.mean([self.kmin, self.kmax])
       self.iter_n = iter_n
    
    def getWeight(self, k):
        return CalcWeightLib.gaussian_pdf(k, self.mean)

    def train(self, data):
        """
        Serial traingin on each HLL estimation
        :param data:
        :return:
        """
        results = []
        weights = []
        for i in xrange(1, self.iter_n):
            hll = BaseHyperLogLog(0.01, i, self.hashFunc)
            for d in data:
                hll.update(d)
            k = hll.calc_cardinality()
            w = self.getWeight(k)
            if i < (RIKEstimator.MAX_REGISTER_INDEX / 2):
                results.append(w * k)
                weights.append(w)

        self.k = sum(results) / sum(weights)


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
        Serial training on each HLL estimation
        :param data:
        :return:
        """
        results = []
        for i in xrange(1, RIKEstimator.MAX_REGISTER_INDEX):
            hll = BaseHyperLogLog(0.01, i, md5_for_vec)
            for d in data:
                hll.update(d)
            if i < (RIKEstimator.MAX_REGISTER_INDEX / 2):
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

class HyperKEstimator(BaseKEstimater):
    """
    The estimator for k value which is used initial k-means
    clustering algorithm with HyperLogLog
    """
    def __init__(self, kmin, kmax, hashFunc, iter_n):
        BaseKEstimater.__init__(self, kmin, kmax, hashFunc)
        self.mean = numpy.mean([self.kmin, self.kmax])
        self.iter_n = iter_n

    def getWeight(self, k):
        return CalcWeightLib.gaussian_pdf(k, self.mean)

    def train(self, data):
        """
        Serial training on each HLL estimation
        :param data:
        :return:
        """
        results = []
        weights = []
        for i in xrange(1, self.iter_n):
            hll = BaseHyperLogLog(0.01, i, self.hashFunc)
            for d in data:
                hll.update(d)
            k = hll.calc_cardinality()
            w = self.getWeight(k)
            if i < (self.iter_n / 2):
                results.append(w * k)
                weights.append(w)
        self.k = sum(results) / sum(weights)