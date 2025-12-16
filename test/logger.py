import logging
import sys

def setup_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    
    logger.setLevel(logging.DEBUG)
    
    log_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(name)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
    )

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(log_formatter)
    stream_handler.setLevel(logging.DEBUG)

    logger.addHandler(stream_handler)

    return logger
