# -*- coding: utf-8 -*-
#因为每个函数都是其它函数的wrapper，只测试通道性

import unittest
from wolfox.fengine.core.d1idiom import *

class ModuleTest(unittest.TestCase):
    def test_swingin(self):
        swingin(np.array([2,3,4,5,6]),np.array([1,2,3,4,5]),3,10)
        self.assertTrue(True)

    def test_swingin1(self):
        swingin1(np.array([2,3,4,5,6]),3,10)
        self.assertTrue(True)

    def test_upconfirm(self):
        upconfirm(np.array([1,2,3,4,5]),np.array([2,3,4,5,6]),np.array([4,5,6,7,8]))
        self.assertTrue(True)

    def test_upveto(self):
        upveto(np.array([1,2,3,4,5]),np.array([2,3,4,5,6]),np.array([4,5,6,7,8]),np.array([1,2,3,4,5]))
        self.assertTrue(True)

    def test_sellconfirm(self):
        sellconfirm(np.array([1,2,3,4,5]),np.array([2,3,4,5,6]),np.array([4,5,6,7,8]),np.array([1,2,3,4,5]))
        self.assertTrue(True)

    def test_simplesell(self):
        simplesell(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),15)
        self.assertTrue(True)

    def test_tsimplesell(self):
        tsimplesell(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),15)
        self.assertTrue(True)

    def test_confirmedsell(self):
        confirmedsell(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),np.array([0,1,2,3,4]),15)
        self.assertTrue(True)

    def test_confirmedsellc(self):
        confirmedsellc(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),15)
        self.assertTrue(True)

    def test_confirmedselll(self):
        confirmedselll(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),np.array([1,2,3,4,5]),np.array([0,1,2,3,4]),15)
        self.assertTrue(True)

    def test_downup(self):
        downup(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),15)
        downup(np.array([0,1,0,0,1]),np.array([1,2,3,4,5]),15,5)
        self.assertTrue(True)

    def test_limit_adjuster(self):
        from wolfox.fengine.core.d1idiom import _limit_adjuster
        self.assertEquals([],_limit_adjuster(np.array([]),np.array([]),3).tolist())
        css = np.array([1,0,0,1,0,1,0,0])
        cls = np.array([1,1,0,0,0,1,1,1])
        self.assertEquals([0,0,1,0,0,0,0,0],_limit_adjuster(css,cls,3).tolist())
        self.assertEquals([0,0,0,1,0,0,0,0],_limit_adjuster(css,cls,2).tolist())

    def test_limit_adjust(self):
        self.assertEquals([],limit_adjust(np.array([]),np.array([]),np.array([]),3).tolist())
        css = np.array([1,0,0,1,0,1,0,0])
        cls = np.array([1,1,0,0,0,1,1,1])
        ts0 = np.array([0,0,0,0,0,0,0,0])
        ts1 = np.array([1,1,1,1,1,1,1,1])
        ts2 = np.array([1,1,0,0,1,1,1,1])
        self.assertEquals([0,0,0,0,0,0,0,0],limit_adjust(css,cls,ts0).tolist())
        self.assertEquals([0,0,1,0,0,0,0,0],limit_adjust(css,cls,ts1).tolist())
        self.assertEquals([0,0,0,1,0,0,0,0],limit_adjust(css,cls,ts1,covered=2).tolist())
        self.assertEquals([0,0,0,0,1,0,0,0],limit_adjust(css,cls,ts2).tolist())


if __name__ == "__main__":
    import logging
    logging.basicConfig(filename="test.log",level=logging.DEBUG,format='%(name)s:%(funcName)s:%(lineno)d:%(asctime)s %(levelname)s %(message)s')
    
    unittest.main()
