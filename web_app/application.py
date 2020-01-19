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


@application.route('/exercisehtml')
def exercisehtml():
    # return requests.get(url="http://workout-gen-pdf.eu-west-2.elasticbeanstalk.com/exercisehtml").content
    pdf = requests.get(url="http://172.31.16.8/exercisehtml").content
    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename='tutorial.pdf')
    response.headers.set('Content-Type', 'applicationlication/pdf')
    return response


if __name__ == '__main__':
    application.run()
