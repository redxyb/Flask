'''
Author: xyb
Date: 2020-08-11 09:55:07
LastEditTime: 2020-08-11 10:11:40
'''
from flask import Flask, abort, g

app = Flask(__name__)


@app.before_request
def authentication():
    """
    利用before_request请求钩子，在进入所有视图前先尝试判断用户身份
    :return:
    """
    # TODO 此处利用鉴权机制（如cookie、session、jwt等）鉴别用户身份信息
    # if 已登录用户，用户有身份信息
    g.user_id = 123


    # else 未登录用户，用户无身份信息
    # g.user_id = None
def login_required(func):
    def wrapper(*args, **kwargs):
        if g.user_id is not None:
            return func(*args, **kwargs)
        else:
            abort(401)

    return wrapper


@app.route('/')
def index():
    return 'home page user_id={}'.format(g.user_id)


@app.route('/profile')
@login_required
def get_user_profile():
    return 'user profile page user_id={}'.format(g.user_id)


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
