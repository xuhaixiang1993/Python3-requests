import os
import unittest
import HTMLTestRunnerCN


import getcwd
from Common.log import log1
from TestCase.testPost import TestPost
from TestCase.testGet import TestGet

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestPost('test_post_one'))
    suite.addTest(TestPost('test_post_two'))
    suite.addTest(TestGet('test_get_one'))
    log1.info('加载测试用例')
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'report/xxx接口自动化测试报告.html')
    try:
        fp = open(file_path, 'wb')
        runner = HTMLTestRunnerCN.HTMLTestReportCN(
            stream=fp,
            title='xxx接口自动化测试报告',
            description='报告中描述部分',
            tester='测试者'
        )
        runner.run(suite)
        log1.info('test end')
        fp.close()
        log1.info('测试报告生成成功')
    except BaseException:
        log1.error('测试报告生成失败', exc_info=1)
    # send_mail()