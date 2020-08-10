'''
Author: xyb
Date: 2020-08-10 11:42:05
LastEditTime: 2020-08-10 12:05:26
'''
'''创建Blueprint'''
from flask import Flask, Blueprint
resource_bp = Blueprint('resource_bp',
                        __name__,
                        static_folder='static',
                        static_url_path='/static',
                        template_folder='templates')

from .views import *