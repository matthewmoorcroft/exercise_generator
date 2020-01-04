from time import time
import logging


def execution_time(method):
    def timed(*args, **kw):
        t_start = time()
        result = method(*args, **kw)
        t_end = time()
        logger = logging.getLogger(method.__name__)
        logger.info(f"Finished execution in {round((t_end-t_start)*1000)}.")

        return result
    return timed
