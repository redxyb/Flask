'''
Author: xyb
Date: 2020-08-08 11:10:13
LastEditTime: 2020-08-08 11:27:28
'''
from flask import Flask, abort
from werkzeug.routing import BaseConverter


class Regex_url(BaseConverter):
    def __init__(self, url_map, *args):
        super(Regex_url, self).__init__(url_map)
        self.regex = args[0]


app = Flask(__name__)
app.url_map.converters['re'] = Regex_url


@app.route('/user/<re("[a-z]{3}"):id>'
           )  #定义访问方式为：http://127.0.0.1:5000/user/xyb
def index(id):
    # abort(404)
    return 'haha,xiaoyuebin %s' % id


@app.errorhandler(404)
def error(e):
    return '这是你意想不到错误，哈哈哈'


if __name__ == "__main__":
    app.run()