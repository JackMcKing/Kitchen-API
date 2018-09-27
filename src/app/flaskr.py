#!flask/bin/python
from flask import Flask, make_response, jsonify


app = Flask(__name__)


@app.route('/douyin/links/api/v1.0/pull', methods=['GET'])
def get_link():
    from sql_handler import SQL_handler as sh
    s = sh(exec='hahaha')
    s.readdata()
    return make_response(jsonify({'url':'http://www.baidu.com'}))


@app.route('/douyin/links/api/v1.0/push', methods=['GET', 'POST'])
def push_link():
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)