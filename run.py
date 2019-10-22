import unittest
from util.utils import CASEPATH,REPORTPATH,get_time
from HTMLTestReportCN import HTMLTestRunner

tests = unittest.defaultTestLoader.discover(CASEPATH)
with open(REPORTPATH+'/'+get_time()+'.html','wb') as f:
    runner = HTMLTestRunner(stream=f,title='guest-master接口测试报告',tester='杨劲松')
    runner.run(tests)