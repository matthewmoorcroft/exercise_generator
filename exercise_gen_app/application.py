import json
from flask import Flask, make_response, render_template
from model import exercise_generator
from time import time
import sys
sys.path.append("/opt/python/current/app/exercise_gen_app")
from .utils.execution_timer import execution_time
import logging
import fpdf
import pdfkit



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

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    t_start = time()
    logger.info("Generating new plan")
    plan = exercise_generator.exercise_builder("4")
    t_end = time()

    pdf.cell(200, 10, txt=str(plan), ln=1, align="C")
    response = make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', filename='tutorial.pdf')
    response.headers.set('Content-Type', 'applicationlication/pdf')

    # pdf.output("tutorial.pdf")
    return response
    # logger.info("Finished generating plan. [RUNTIME: " +
    #             str(round((t_end - t_start)*1000)) + " ms]")


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
    path_wkhtmltopdf = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
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
    return html


if __name__ == "__main__":

    application.run()
