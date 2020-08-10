'''
Author: xyb
Date: 2020-08-10 18:35:32
LastEditTime: 2020-08-10 18:52:50
'''
from flask import Flask, make_response, request

app = Flask(__name__)
app.secret_key = 'dfslkfjdlfsdkjfnskj'  #直接设置
#间接设置
# class DefaultConfig(object):
#     SECRET_KEY = 'dfslkfjdlfsdkjfnskj'
# app.config.from_object(DefaultConfig)


@app.route('/set_session')
def set_session():
    session['username'] = 'xyb'
    return 'set seccion is ok'


@app.route('/get_session')
def get_session():
    username = session.get('username')
    return 'get session username {}'.format(username)


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
