import logging
from multiprocessing import Pool
from datetime import datetime

logging.basicConfig(filename='logs/app.log', level=logging.DEBUG)

def add_numbers(pair):
    try:
        result = sum(pair)
        logging.info(f"Adding {pair}: {result}")
        return result
    except Exception as e:
        logging.error(f"Error adding {pair}: {str(e)}")
        raise e

def process_addition_request(payload):
    started_at = datetime.now()
    logging.info(f"Processing started at {started_at}")
    try:
        with Pool(processes=4) as pool:
            results = pool.map(add_numbers, payload)
        status = "complete"
    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        results = []
        status = "error"
    completed_at = datetime.now()
    logging.info(f"Processing completed at {completed_at}")
    return results, status, started_at, completed_at
