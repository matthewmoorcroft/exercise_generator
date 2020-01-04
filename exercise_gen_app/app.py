import logging
import fpdf
from .utils.execution_timer import execution_time
from time import time
from .model import exercise_generator
from flask import Flask, make_response

app = Flask(__name__)

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


@app.route('/generator')
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
    response.headers.set('Content-Type', 'application/pdf')

    # pdf.output("tutorial.pdf")
    return response
    # logger.info("Finished generating plan. [RUNTIME: " +
    #             str(round((t_end - t_start)*1000)) + " ms]")


#
# if __name__ == "__main__":
#
#     main()
