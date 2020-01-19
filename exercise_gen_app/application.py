import logging
import pdfkit
from utils.execution_timer import execution_time
from time import time
from model import exercise_generator
from flask import Flask, make_response, render_template
import json
# import sys
# sys.path.append("/opt/python/current/app/exercise_gen_app")


application = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s:%(levelname)s:%(module)s:%(message)s')

file_handler = logging.FileHandler('exercise_gen.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


@application.route('/generator')
@execution_time
def generator():

    t_start = time()
    # with open('exercises.json', 'r') as json_file:
    #     exercises = json.load(json_file)
    plan = exercise_generator.exercise_builder("4")
    t_end = time()
    days = len(plan[0])
    # pdf.output("tutorial.pdf")
    html = render_template('exercises.html', days=days, exercises=plan)
    # path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    path_wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"
    options = {
        'page-size': 'A4',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None,
        'disable-smart-shrinking': ''
    }
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, False, configuration=config, options=options)
    response = make_response(pdf)
    response.headers.set('Content-Disposition', 'attachment', filename='workout.pdf')
    response.headers.set('Content-Type', 'applicationlication/pdf')
    return response


@application.route('/html')
# @execution_time
def generator_html():

    # t_start = time()
    # with open('exercises.json', 'r') as json_file:
    #     exercises = json.load(json_file)
    plan = exercise_generator.exercise_builder("4")
    # t_end = time()
    days = len(plan[0])
    # pdf.output("tutorial.pdf")
    html = render_template('exercises.html', days=days, exercises=plan)

    return html


@application.route('/exercisehtml')
# @execution_time
def exercise_htm():

    t_start = time()
    with open('exercises.json', 'r') as json_file:
        exercises = json.load(json_file)
    t_end = time()
    days = len(exercises[0])
    # pdf.output("tutorial.pdf")
    html = render_template('exercises.html', days=days, exercises=exercises)
    # path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    path_wkhtmltopdf = "/usr/local/bin/wkhtmltopdf"
    options = {
        'page-size': 'A4',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None,
        'disable-smart-shrinking': ''
    }
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html, "out.pdf", configuration=config, options=options)
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename='tutorial.pdf')
    response.headers.set('Content-Type', 'applicationlication/pdf')
    return response


if __name__ == "__main__":

    application.run(port=5001)
