'''
Author: xyb
Date: 2020-08-11 08:54:33
LastEditTime: 2020-08-11 09:35:42
'''
'''
Flask上下文对象:相当于一个容器，保存了Flask程序运行过程中的一些信息
1.请求上下文(request context):对象有request、session
2.应用上下文(application context):对象有current_app、g
current_app中存储的一些变量：
a.应用的启动脚本是哪个文件，启动时指定哪些参数
b.加载了哪些配置文件，导入了哪些配置
c.连了哪个数据库
d.有哪些public的工具类、常量
e.应用跑在哪个机器上，ip多少，内存多大
'''
from flask import Flask, request, current_app

app1 = Flask(__name__)
app2 = Flask(__name__)

app1.redis_cli = 'app1 redis client'
app2.redis_cli = 'app2 redis client'


@app1.route('/route11')
def route11():
    return current_app.redis_cli


@app1.route('/route12')
def route12():
    return current_app.redis_cli


@app2.route('/route21')
def route21():
    return current_app.redis_cli


@app2.route('/route22')
def route22():
    return current_app.redis_cli


if __name__ == "__main__":
    app1.run(host='', port=5000, debug=False)
    app2.run(host='', port=5000, debug=False)
