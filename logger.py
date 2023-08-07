import logging
import os
import sys

def configure_logger():
    LOG_LEVEL = logging.INFO 

    if 'LOG_LEVEL' in os.environ:
        level = os.environ['LOG_LEVEL'].upper()
        if level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            LOG_LEVEL = getattr(logging, level)

    logging.basicConfig(stream=sys.stdout, level=LOG_LEVEL, format='%(asctime)s - %(levelname)s - %(message)s')

    return logging.getLogger()

