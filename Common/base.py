# -*- conding:UTF-8 -*-
import unittest
import requests
import os
import configparser

import getcwd
from Common.log import log1
from Common.configOverWriter import configOverWrite

path = getcwd.get_cwd()
config_path = os.path.join(path, 'config.ini')
config = configOverWrite()
config.read(config_path, encoding='utf-8-sig')


class Base(unittest.TestCase):
    """测试基类"""

    def get(self, url, params=None, headers=None, files=None, auth=None):
        """get请求，返回响应码和响应实体"""
        try:
            r = requests.get(url, params=params, headers=headers, files=files, auth=auth, verify=False, stream=True, timeout=10)
            log1.info('请求实体内容：%s' % params)
            status_code = r.status_code
            log1.info('返回状态码：%d' % status_code)
            response = r.json()
            log1.info('响应实体内容：%s' % response)
            return status_code, response
        except BaseException:
            log1.error('请求失败!', exc_info=1)

    def post(self, url, data=None, headers=None, files=None, auth=None):
        """post请求，返回响应码和响应实体"""
        try:
            r = requests.post(url, data=data, headers=headers, files=files, auth =auth, verify=False, timeout=10)
            log1.info('请求实体内容：%s' % data)
            status_code = r.status_code
            log1.info('返回状态码：%d' % status_code)
            response = r.json()
            log1.info('响应实体内容：%s' % response)
            return status_code, response
        except BaseException:
            log1.error('请求失败!', exc_info=1)

    def post_json(self, url, data=None, headers=None, auth=None):
        """post请求，使用json格式提交请求实体，返回响应码和响应实体"""
        try:
            r = requests.post(url, json=data, headers=headers, auth=auth, verify=False, timeout=10)
            log1.info('请求实体内容：%s' % data)
            status_code = r.status_code
            log1.info('返回状态码：%d' % status_code)
            response = r.json()
            log1.info('响应实体内容：%s' % response)
            return status_code, response
        except BaseException:
            log1.error('请求失败!', exc_info=1)

    def config_read(self, section, key=None, url=None):
        """从配置文件中读取"""
        try:
            # key是url，拼接url返回
            if key == 'url':
                config_url = config.get(section, key)
                url = config_url+url
                log1.info('请求的url：%s' % url)
                return url
            # 读取section下所有key
            elif key is None:
                config_get = config.options(section)
                log1.info('读取%s下%s=%s' % (section, key, config_get))
                return config_get
            else:
                # 读取section下key的值
                config_get = config.get(section, key)
                log1.info('读取%s下所有key：%s' % (section, config_get))
                return config_get
        except configparser.NoSectionError:
            log1.error('section is not in config', exc_info=1)
        except configparser.NoOptionError:
            log1.error('key is not in config', exc_info=1)

    def config_write(self, section, key=None, value=None):
        """往配置文件中写入"""
        try:
            # 在section下新增key = value
            if key is not None and value is not None:
                config.set(section, key, value)
                with open(config_path, 'w', encoding='utf-8') as f:
                    config.write(f)
                log1.info('在section:%s下添加%s=%s' % (section, key, value))
            else:
                # 新增section
                config.add_section(section)
                with open(config_path, 'w', encoding='utf-8') as f:
                    config.write(f)
                log1.info('新增section：%s' % section)
        except configparser.NoSectionError:
            log1.error('section is not in config', exc_info=1)
        except configparser.NoOptionError:
            log1.error('key is not in config', exc_info=1)

    def config_remove(self, section, key=None):
        """从配置文件中删除"""
        try:
            # 在section下删除key
            if key is not None:
                config.remove_option(section, key)
                with open(config_path,'w', encoding='utf-8') as f:
                    config.write(f)
                log1.info('在section：%s下删除键：%s' % (section, key))
            else:
                # 删除section
                config.remove_section(section)
                with open(config_path, 'w', encoding='utf-8') as f:
                    config.write(f)
                log1.info('删除section:%s' % section)
        except configparser.NoSectionError:
            log1.error('section is not in config', exc_info=1)
        except configparser.NoOptionError:
            log1.error('key is not in config', exc_info=1)

    def dict_value(self, dict1, obj, defaule=None):
        """查找嵌套字典中key对应的值"""
        try:
            for k, v in dict1.items():
                if k == obj:
                    log1.info('嵌套字典中%s对应的值为%s' % (obj, v))
                    return v
                else:
                    if type(v) is dict:
                        re = self.dict_value(v, obj, defaule)
                        if re is not defaule:
                            return re
        except BaseException:
            log1.error('可能有非字典嵌套', exc_info=1)

    def get_addkey(self, user):
        """遍历获得配置文件收件人email"""
        sum1 = 0
        L = []
        for i in user:
            if sum1 < len(user):
                emails = self.config_read('addressed', i)
                L.append(emails)
                sum1 += 1
        return L
