'''
Author: xyb
Date: 2020-08-09 15:26:09
LastEditTime: 2020-08-10 08:12:28
'''
from flask import Flask
from werkzeug.routing import BaseConverter
import json


class Regex_url(BaseConverter):
    def __init__(self, url_map, *args):
        super(Regex_url, self).__init__(url_map)
        self.regex = args[0]


app = Flask(__name__,
            static_url_path='/xyb',
            static_folder='static',
            template_folder='templates')

app.url_map.converters['re'] = Regex_url


@app.route('/')
def homepage():
    return 'this is a home page'


@app.route('/index/<re("[a-z]{3}"):id>', methods=["GET", "POST"])
def index(id):
    return 'haha,this is %s' % id


@app.errorhandler(404)
def error():
    return 'zhe page is not found,please try it again!'


@app.route('/route_map')
def route_map():
    #路由遍历
    for rule in app.url_map.iter_rules():
        print('name={} path={}'.format(rule.endpoint, rule.rule))
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})


#遍历路由信息

if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)
