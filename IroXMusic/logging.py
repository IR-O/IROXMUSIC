import logging.config
import sys

# Define the log configuration
log_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s - %(levelname)s] - %(name)s - %(message)s'
        },
    },
    'handlers': {
        'default': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'level': logging.INFO,
            'stream': sys.stdout,
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard',
            'level': logging.INFO,
            'filename': 'log.txt',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'file'],
            'level': logging.INFO,
            'propagate': True,
        },
        'httpx': {
            'handlers': ['file'],
            'level': logging.ERROR,
            'propagate': True,
        },
    },
}

# Configure the logging module with the log configuration
logging.config.dictConfig(log_config)

# Get the logger
logger = logging.getLogger()

# Example log message
logger.info('This is an info message')
