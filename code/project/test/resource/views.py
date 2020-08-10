'''
Author: xyb
Date: 2020-08-10 11:42:16
LastEditTime: 2020-08-10 12:08:34
'''
'''注册resource的路由'''

from . import resource_bp


@resource_bp.route('/index', methods=['POST', 'GET'])
def resource_page():
    return 'this is a resource page'
