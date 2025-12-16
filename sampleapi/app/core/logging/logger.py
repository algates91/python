import logging
import sys

def setup_custom_logger(name):
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger
    # Ensure logger will emit INFO-level (or higher) messages. By default
    # a newly created logger inherits level WARNING, which would hide INFO.
    logger.setLevel(logging.INFO)

    # Prevent messages from being propagated to the root logger (avoid duplicates)
    logger.propagate = False

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger