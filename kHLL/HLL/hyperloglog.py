__author__ = "shoe116"

class HLLRegister(list):
    def __init__(self, registerIndexSize):
        list.__init__(self)
        self.registerIndexSize = registerIndexSize
        self.mask = int('1' * registerIndexSize, 2)

        ## all value is 0 as init
        for i in xrange(0, 2**registerIndexSize):
            self.append(0)
        
    def update(self, hashValue):
        index = self._calcindex(hashValue)
        value = self._calcvalue(hashValue)
        if value > self[index]:
            self[index] = value

    def _calcindex(self, hashValue):
        return self.mask & hashValue

    def _calcvalue(self, hashValue):
        value = hashValue >> self.registerIndexSize
        ## search min flaged bit 
        return format(value, 'b')[::-1].index('1') + 1

class BaseHyperLogLog(object):
    def __init__(self, constant, registerIndexSize, hashFunc):
        self.constant = constant
        self.registerIndexSize = registerIndexSize
        self.hashFunc = hashFunc
        self.register = HLLRegister(registerIndexSize)

    def calc_cardinality(self):
        invs = map(lambda x: 2**(-x), self.register)
        return self.constant * (len(self.register)**2) / sum(invs)

    def update(self, data):
        self.register.update(self.hashFunc(data))

