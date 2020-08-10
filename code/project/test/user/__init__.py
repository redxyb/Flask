'''
Author: xyb
Date: 2020-08-10 09:46:17
LastEditTime: 2020-08-10 12:06:56
'''
'''用来创建蓝图对象'''
from flask import Flask, Blueprint
user_bp = Blueprint('user_bp',
                    __name__,
                    static_folder='static',
                    static_url_path='/static',
                    template_folder='templates')

from .views import *