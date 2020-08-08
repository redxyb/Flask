'''
Author: xyb
Date: 2020-08-08 11:59:25
LastEditTime: 2020-08-08 17:46:43
'''
from flask import Flask, make_response, request

app = Flask(__name__, static_url_path='/static', static_folder='static')


#设置cookie
@app.route('/cookie')
def set_cookie():
    resp = make_response('this is to set cookie')
    resp.set_cookie('username', 'xyb')
    return resp


#获取cookie
@app.route('/request')
def get_cookie():
    resp = request.cookies.get('username')
    return resp


if __name__ == "__main__":
    app.run(host="", port=5000, debug=True)  #可自己更改
