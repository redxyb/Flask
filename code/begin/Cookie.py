'''
Author: xyb
Date: 2020-08-10 18:06:52
LastEditTime: 2020-08-10 18:34:28
'''
from flask import Flask, make_response, redirect, request

app = Flask(__name__)


#设置cookie
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('set_cookie ok')
    resp.set_cookie('username', 'xyb', max_age=3600)  #max_age:有效期
    return resp


#读取cookie
@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


#删除cookie
@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response("hello,xyb")
    resp.delete_cookie('username')
    return resp


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
