'''
Author: xyb
Date: 2020-08-10 15:09:13
LastEditTime: 2020-08-10 18:05:45
'''
from flask import Flask, render_template, redirect, jsonify, make_response

app = Flask(__name__,
            static_url_path='/static',
            static_folder='static',
            template_folder='templates')


#返回模板
@app.route('/')
def index():
    mstr = 'hello,我是xiaoyuebin'
    mint = 10
    return render_template('index.html', my_str=mstr, my_int=mint)


#重定向
@app.route('/test')
def test():
    return redirect('http://www.baidu.com')


#返回JSON
@app.route('/test1')
def test1():
    json_dict = {"user_id": 10, "user_name": 'laoyinbi'}
    return jsonify(json_dict)


#自定义状态码:有错误
# @app.route('test2')
# def test2():
#     return ('状态码为 666', 666, {'study': 'python'})


#make_response方式
@app.route('/test3')
def test3():
    resp = make_response('make response测试')
    resp.headers["name"] = "python"
    resp.status = "404 not found"
    return resp


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
