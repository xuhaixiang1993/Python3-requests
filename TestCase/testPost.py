import unittest

from Common.base import Base
from Logs.log import log1


class TestPost(unittest.TestCase):
    """测试post请求
    github接口文档
    https://developer.github.com/v3/users/emails/"""

    def test_post_one(self):
        """调用github添加邮箱接口"""
        case_name = '添加邮箱'
        log1.info("执行测试用例：%s" % case_name)
        try:
            postone = Base()
            url = postone.config_read('test', 'url', url='/user/emails')
            # 想要添加的邮箱，请求实体
            payloda = {'emails': ['xxx@163.com', 'xxx@qq.com']}
            # github用户名和密码
            auth = ('username', 'password')
            status_code, response_json = postone.post_json(url, data=payloda, auth=auth)
            if status_code is 201:
                log1.info('测试用例执行成功：%s' % case_name)
        except BaseException:
            log1.error("测试用例执行出错：%s" % case_name, exc_info=1)
            raise

    def test_post_two(self):
        """验证执行失败，测试报告是否会统计"""
        case_name = '测试失败'
        log1.info("执行测试用例：%s" % case_name)
        try:
            postone = Base()
            # url地址少了/
            url = postone.config_read('test', 'url', url='user/emails')
            payloda = {'emails': ['xxx@163.com', 'xxx@qq.com']}
            auth = ('username', 'password')
            status_code, response_json = postone.post_json(url, data=payloda, auth=auth)
            if status_code is 201:
                log1.info('测试用例执行成功：%s' % case_name)
        except BaseException:
            log1.error("测试用例执行出错：%s" % case_name, exc_info=1)
            raise
