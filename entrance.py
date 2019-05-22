import os
import unittest
import HTMLTestRunnerCN

from TestCase.testPost import TestPost
from TestCase.testGet import TestGet
from Common.sendMail import send_mail
import getcwd


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPost('test_post_one'))
    suite.addTest(TestPost('test_post_two'))
    suite.addTest(TestGet('test_get_one'))
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'report/xxx接口自动化测试报告.html')
    fp = open(file_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='xxx接口自动化测试报告',
        description='报告中描述部分',
        tester='测试者'
    )
    runner.run(suite)
    fp.close()
    # send_mail()