'''
Author: xyb
Date: 2020-08-10 14:22:55
LastEditTime: 2020-08-10 14:54:54
'''
from flask import Flask, request
from werkzeug.routing import BaseConverter


class MobileConverter(BaseConverter):
    '''手机号格式'''
    regex = r'1[3-9]\d{9}'  #注意regex名字固定


#将自定义的转换器告知Flask应用
app = Flask(__name__)
#将自定义的转换器添加到转换器字典中，并指定转换器使用时的名字为：mobile
app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms_code/<mobile:mob_num>'
           )  #http://127.0.0.1:5000/sms_code/13873052522
def send_sms_code(mob_num):
    return 'send sms code to {}'.format(mob_num)


@app.route('/articles')  #http://127.0.0.1:5000/articles?channel_id=1
def get_articles():
    channel_id = request.args.get('channel_id')
    return 'you wanna get articles of channel {}'.format(channel_id)


@app.route('/upload')
def upload_file():
    f = request.files['pic']
    with open('./static/image/1.jpg', 'wb') as new_file:
        new_file.write(f.read())
    f.save('./1.jpg')
    return 'ok'


if __name__ == "__main__":
    app.run(host='', port=5000, debug=False)