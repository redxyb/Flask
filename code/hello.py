'''
Author: xyb
Date: 2020-08-08 10:02:55
LastEditTime: 2020-08-08 11:09:13
'''
from flask import Flask, abort, redirect

#Flask类接收一个参数__name__
app = Flask(__name__)


#装饰器的作用是将路由映射到视图函数index
@app.route('/')
def index():
    # abort(404)  #出现异常错误，用来立即终止视图函数的执行
    # return 'hello world', 999  #返回状态码
    return redirect('http://www.baidu.com')  #重定向redirect示例


@app.errorhandler(404)  #errorhandler()接收的参数为异常状态码
def error(e):
    return '您请求的页面不存在了，请确认后再次访问！%s' % e


#Flask应用程序实例的run方法启动web服务器
if __name__ == '__main__':
    app.run()