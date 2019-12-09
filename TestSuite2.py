import unittest
from TestCompany1 import TestCompany1
from TestCompany2 import TestCompany2
from TestPrice import TestPrice
from TestProperty import TestProperty

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestCompany1))
    suite.addTest(unittest.makeSuite(TestCompany2))
    suite.addTest(unittest.makeSuite(TestPrice))
    suite.addTest(unittest.makeSuite(TestProperty))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
