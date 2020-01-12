from flask import Flask, render_template
import requests
application = Flask(__name__)


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/generator')
def generator():
    return requests.get(url="workout-gen-pdf.eu-west-2.elasticbeanstalk.com/generator").content


@application.route('/exercisehtml')
def exercisehtml():
    return requests.get(url="workout-gen-pdf.eu-west-2.elasticbeanstalk.com/exercisehtml").content


if __name__ == '__main__':
    application.run()
