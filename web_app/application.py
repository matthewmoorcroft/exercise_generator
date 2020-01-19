from flask import Flask, render_template, make_response
import requests
application = Flask(__name__)


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/generator')
def generator():
    pdf = requests.get(url="http://172.31.16.8/generator").content
    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename='tutorial.pdf')
    response.headers.set('Content-Type', 'applicationlication/pdf')
    return response


if __name__ == '__main__':
    application.run()
