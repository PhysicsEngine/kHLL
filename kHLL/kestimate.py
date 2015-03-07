from HLL.hyperloglog import BaseHyperLogLog
from abc import abstractmethod

class BaseKEstimater(object):

    def __init__(self, kmin, kmax, hashFunc):
        self.kmin = kmin
        self.kmax = kmax
        self.hashFunc = hashFunc
        self.k = 0

    def getK(self):
        return int(self.k)

    @abstractmethod
    def train(self, data):
        pass

