from abc import abstractmethod
from scipy.stats import norm

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

class GaussianWeight(object):
    def __init__(self, mean):
        self.mean = mean
    
    def pdf(self, value):
        return norm.pdf(value, self.mean)
