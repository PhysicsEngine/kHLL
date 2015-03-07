__author__ = 'shoe116'

import unittest
from HLL.hyperloglog import HLLRegister, BaseHyperLogLog

class TestHyperLogLogHash(unittest.TestCase):
    HASH = 172986408
    REGISTER_INDEX_SIZE = 6
    INDEX = 40
    VALUE = 7

    def test__calcindex(self):
        register = HLLRegister(self.REGISTER_INDEX_SIZE)
        self.assertEqual(self.INDEX, register._calcindex(self.HASH))

    def test__calcvalue(self):
        register = HLLRegister(self.REGISTER_INDEX_SIZE)
        self.assertEqual(self.VALUE, register._calcvalue(self.HASH))

    def test_update(self):
        register = HLLRegister(self.REGISTER_INDEX_SIZE)

        ## before
        self.assertEqual(0, register[self.INDEX])

        ## after
        register.update(self.HASH)
        self.assertEqual(self.VALUE, register[self.INDEX])

class TestBaseHyperLogLogHash(unittest.TestCase):

    ## it is not good test :-(
    def test_calc_cardinality(self):
        hll = BaseHyperLogLog(1.0/64, 6, None)
        hll.register[51] = 2
        self.assertEqual(1, int(hll.calc_cardinality()))

if __name__ == '__main__':
    unittest.main()
