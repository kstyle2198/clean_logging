from utils.setlogger import setup_logger
import logging
logger = setup_logger(f"{__name__}", level=logging.INFO)


def process_01():
    logger.info("Main function started")
    try:
        # Simulate some operations
        x = 1 / 0  # This will raise an exception
    except ZeroDivisionError as e:
        logger.error(f"An error occurred: {e}")
    logger.info("Main function ended")

