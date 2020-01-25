from flask import Flask, render_template, make_response
import requests
application = Flask(__name__)


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/generator')
def generator():
    pdf = requests.get(url="http://ip-172-31-43-191.eu-west-2.compute.internal/generator").content
    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename='workout.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response


@application.route('/exercisehtml')
def exercisehtml():
    # return requests.get(url="http://workout-gen-pdf.eu-west-2.elasticbeanstalk.com/exercisehtml").content
    pdf = requests.get(
        url="http://ip-172-31-43-191.eu-west-2.compute.internal/exercisehtml").content
    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename='tutorial.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response


if __name__ == '__main__':
    application.run()
