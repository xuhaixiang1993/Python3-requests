from Common.base import Base

section = 'login'
username = '测试'
password = '一下'

s = Base()

s.config_write(section)
s.config_write(section, 'username', username)
s.config_write(section, 'password', password)

url = s.config_read('test', 'url', url='test/test1')
get_username = s.config_read(section, 'username')
get_password = s.config_read(section, 'password')

s.config_delete(section, 'usrename', )
s.config_delete(section, 'password')
s.config_delete(section)