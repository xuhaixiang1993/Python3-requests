# Python-Requests
接口测试框架，生成测试报告，发送邮件

1）log使用
建议直接在log.py下创建实例来输出日志，在使用时直接import该实例即可。避免重复创建和偶尔info日志重复输出的问题。

2）Base.py
这里是测试基类，封装了对ini配置文件操作，get/post请求，对响应实体的操作，和一起发送邮件时，获取收件人的方法。
2.1 配置文件操作
config_read()：可以传入section，key，url三个参数。
当只传入section和key时，返回section对应key的值。
	
