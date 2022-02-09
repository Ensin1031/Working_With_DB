import logging
import logging.handlers
import logging.config

DEBUG = True

LOGGING_CONF = {
    "disable_existing_loggers": True,
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "{asctime} - {name}: -> {levelname} - {message}",
            "datefmt": "%d:%m:%Y - %H:%M:%S",
            "style" : "{",
        },
        "brief": {
            "format": "%(levelname)-8s %(asctime)s %(name)-16s %(message)s",
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "brief",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "verbose",
            "filename": "logs/log.log",
            "encoding": "utf-8",
            "mode": "a",
            "maxBytes": 10485760,
            "backupCount": 5,
        },
    },
    "loggers": {
        "main": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        },
        "db": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
        },
    },
}

logging.config.dictConfig(LOGGING_CONF)

# logg = logging.getLogger("main")
# logg.debug("loggers %s configured", ", ".join(LOGGING_CONF["loggers"]))