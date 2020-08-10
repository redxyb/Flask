'''
Author: xyb
Date: 2020-08-09 09:29:16
LastEditTime: 2020-08-09 11:21:42
'''
from flask import Flask, make_response, request, redirect

# class DefaultConfig(object):
#     '''默认配置类:可以被继承'''
#     SECRET_KEY = 'sfsfsdfgsgfsferytfhfyguiyt'

# class DevelopmentConfig(DefaultConfig):
#     '''扩展配置，继承自默认配置'''
#     DEBUG = True

app = Flask(__name__,
            static_url_path='/xyb',
            static_folder='static',
            template_folder='templates',
            static_host='')

#从配置对象中加载设置
#app.config.from_object(DefaultConfig)
#从配置文件中加载设置
app.config.from_pyfile('setting.py')


@app.route('/')
def index():
    print(app.config['SECRET_KEY'])
    print(app.url_map)
    return 'haha,xiaoyuebin'


if __name__ == "__main__":
    app.run(
        host='',  #服务器主机地址
        port=5000,  #端口号
        debug='False')  #是否开启调试：开启，修改代码会自动重新运行
