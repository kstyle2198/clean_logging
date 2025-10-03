import logging
from utils.setlogger import setup_logger
logger = setup_logger(f"{__name__}", level=logging.INFO)

from process.ps import process_01

if __name__ == "__main__":
    try:
        logger.info("Program started")
        process_01()
        logger.info("Program ended successfully")
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
             