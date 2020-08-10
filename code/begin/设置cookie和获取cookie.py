'''
Author: xyb
Date: 2020-08-08 11:59:25
LastEditTime: 2020-08-09 09:22:17
'''
from flask import Flask, make_response, request

app = Flask(
    __name__,  #Flask程序所在的包
    static_url_path='/static',  #静态文件访问路径
    static_folder='static',  #静态文件存储的文件夹
    template_folder='templates')  #模板文件存储的文件夹
#直接访问静态文件:http://127.0.0.1:5000/xyb/image/kobe.jpg


#设置cookie
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'xyb')
    return resp


#获取cookie
@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


if __name__ == "__main__":
    app.run(host="", port=5000, debug=True)  #可自己更改
