# Python-Requests
接口测试框架，生成测试报告，发送邮件

1）Logs日志文件
log.py：日志功能实现文件，建议直接在log.py下创建实例来输出日志，在使用时直接import该实例即可。避免重复创建和偶尔info日志重复输出的问题。
loginTest.py：日志功能测试文件



![配置文件图片](https://github.com/xuhaixiang1993/Python3-requests/blob/master/picture/config.jpg)

2）配置文件
配置文件已[]括起来的是section，下面已key，value存放配置信息
test:测试环境的一些参数，项目中接口url，前面一部分地址都是相同的，所以可以把前部分url放在配置文件中。后部分通过方法中参数拼接成该接口的url。这样想要在不同环境跑同一套代码，只需要更改配置文件中的url
sender：发件人的信息，比如发件人姓名，发件人邮箱，对应邮箱的SMTP授权码。
addressed:收件人的邮箱

3）Base.py
这里是测试基类，封装了对ini配置文件操作，get/post请求，对响应实体的操作，发送邮件时，获取收件人的方法。

    3.1 配置文件操作
	config_read()：可以传入section，key，url三个参数。
	当只传入section和key时，返回section对应key的值。
    当全都传时，表示拼接该接口的url。url参数应该已 /路径/路径 这样的形式
    
    config_write():可以传入section, key, value三个参数。
    当只传入section时，在配置文件中新增section
    当全都传入时，在section下新增key, value
    
    config_remove():可以传入section, key两个参数。
    当只传入section时，在删除文件中删除对应section
    当全都传入时，删除section下对应key, value
    
    3.2 get/post请求
    get()：get请求      post()：post请求        post_json()：post请求，json格式传请求实体
    
    url：接口的url地址，通过config_read()方法拼接url获得
    config_read('/user/emails')
    
    params/data：接口的请求实体，需要已字典形式传参
    {'email':'xxxx@qq.com'}
    
    headers：请求头，需要已字典形式传参 
    {'Host':'www.baoi.com'}
    
    files：上传下载文件，
    上传:{'接口中对应字段':open(path.'rb')} path:需要上传文件的路径
    下载:whith open(path,'wb') as f; f.write(r.content)
    
    stream：默认为True，推迟下载响应体
    
    auth：auth认证   
    （'username','password）
    
    verify:默认Flase,跳过SLL认证
    
    timeout：超时时间，默认10秒
    
    3.3 从响应体，多层dict中查找key的值
    dict_value(): dict参数 想要查找的多层嵌套字典 obj想要查询value的key
    
    3.4 发送邮件配置
    config_options()：用来读取配置文件中收件人姓名
    get_addkey():用来读取配置文件中收件人邮箱
    
    
