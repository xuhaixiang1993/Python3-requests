from Logs.log import log1
try:
    log1.info("开始测试")
    r = 10/0
    log1.info("resuit:",r)
except ZeroDivisionError as e :
    log1.error("报错信息：",exc_info = 1)
log1.info('end')