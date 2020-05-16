import logging
import sys
from pathlib import Path

from loguru import logger

from boil import conf


def init_logging():
    config = {
        'handlers': [
            {
                'sink': Path(conf.root_dir) / conf.log_file,
                'level': 'DEBUG',
                'rotation': '1 week',
            },
        ],
    }
    if conf.stdout_log:
        config['handlers'].append({
            'sink': sys.stdout,
            'level': 'DEBUG',
        })
    logger.configure(**config)

    class InterceptHandler(logging.Handler):
        def emit(self, record):
            logger_opt = logger.opt(depth=6, exception=record.exc_info)
            logger_opt.log(record.levelname, record.getMessage())

    logging.getLogger().setLevel(logging.DEBUG)
    if conf.sql_log:
        logging.getLogger('sqlalchemy').setLevel(logging.DEBUG)
    logging.getLogger().addHandler(InterceptHandler())
