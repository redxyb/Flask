'''
Author: xyb
Date: 2020-08-10 09:44:39
LastEditTime: 2020-08-10 11:52:50
'''
'''启动文件'''
from flask import Flask, Blueprint
from user import user_bp
from resource import resource_bp

app = Flask(__name__,
            static_url_path='/xyb',
            static_folder='static',
            template_folder='templates')

#在应用中注册blueprint
app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(resource_bp, url_prefix='/resource')


#注册主路由
@app.route('/', methods=['POST', 'GET'])
def index():
    return 'this is a home page!'


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
