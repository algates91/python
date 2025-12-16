import logging
import sys

def setup_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)
    
    log_formatter = logging.Formatter(
        '%(asctime)s - [%(levelname)s] - %(name)s - %(message)s ',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    log_handler = logging.StreamHandler(sys.stdout)

    log_handler.setFormatter(log_formatter)
    log_handler.setLevel(logging.DEBUG)
    logger.addHandler(log_handler)

    return logger