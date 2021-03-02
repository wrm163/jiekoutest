import unittest

from HTMLTestRunner import HTMLTestRunner
import os
suite = unittest.TestSuite()

tests = unittest.defaultTestLoader.discover(os.getcwd(),"*test.py")
suite.addTest(tests)

f = open("讲师评价系统测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream = f,
    verbosity = 1,
    title = "讲师评价系统"
)
runner.run(suite)
