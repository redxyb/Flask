'''
Author: xyb
Date: 2020-08-11 11:01:41
LastEditTime: 2020-08-11 11:12:42
'''
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


class HelloWorldResource(Resource):
    def get(self):
        return {'hello': 'world'}

        def post(self):
            return {'msg': 'post hello world'}


api.add_resource(HelloWorldResource, '/',
                 endpoint='HelloWorld')  #endpoint参数为路由起名

if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)