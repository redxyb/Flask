'''
Author: xyb
Date: 2020-08-10 10:17:07
LastEditTime: 2020-08-10 12:18:19
'''
'''注册user的路由'''
from . import user_bp
from flask import Flask, url_for, redirect


@user_bp.route('/index', methods=['GET', 'POST'])
def user_profile():
    return 'user_profile'


#动态路由：<>即是一个转换器，默认为字符串类型，
#即将该位置的数据以字符串格式进行匹配、并以字符串为数据类型类型、
#user_id为参数名传入视图
@user_bp.route('/user<int(min=1,max=100):user_id>')  #整型，user_id最小为1，最大为100
# @user_bp.route('/user<:user_id>')
def user_info(user_id):
    return 'hello user {}'.format(user_id)


#重定向路由：重定向到其他蓝图的路径方法
@user_bp.route('/redirect')
def re():
    return redirect(url_for('resource_bp.resource_page'))
