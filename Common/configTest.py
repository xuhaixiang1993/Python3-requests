from Common.base import Base

section = '我要'
username = '测试'
password = '一下'

config = Base()

config.config_write(section)
config.config_write(section, 'username', username)
config.config_write(section, 'password', password)

url = config.config_read('test', 'url', url='test/test1')
get_username = config.config_read(section, 'username')
get_password = config.config_read(section, 'password')

config.config_remove(section, 'usrename', )
config.config_remove(section, 'password')
config.config_remove(section)