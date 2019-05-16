import unittest

from Common.base import Base
from Logs.log import log1


class TestGet(unittest.TestCase):
    """测试get请求
    github接口文档
    https://developer.github.com/v3/users/emails/"""

    def test_get_one(self):
        """调用github查询邮箱接口"""
        case_name = '查询邮箱'
        log1.info("执行测试用例：%s" % case_name)
        try:
            getone = Base()
            url = getone.config_read('test', 'url', url='/user/emails')
            # github用户名和密码
            auth = ('username', 'password')
            status_code, response_json = getone.get(url, auth=auth)
            if status_code is 200:
                log1.info('测试用例执行成功：%s' % case_name)
        except BaseException:
            log1.error("测试用例执行出错：%s" % case_name, exc_info=1)
            raise
