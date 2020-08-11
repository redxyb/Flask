'''
Author: xyb
Date: 2020-08-11 07:26:18
LastEditTime: 2020-08-11 07:37:40
'''
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    title = 'index'
    my_str = 'xyb'
    my_int = '22'
    return render_template('index.html',
                           title=title,
                           my_str=my_str,
                           my_int=my_int)


#errorhandler装饰器：注册一个错误程序，当程序抛出指定错误状态码时，就会调用该装饰器中的方法
@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'


#捕获指定异常
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
