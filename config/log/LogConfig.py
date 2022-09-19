import logging.config

__config = {
    "version": 1,
    "formatters": {
        "simple": {"format": "[%(name)s] %(message)s"},
        "complex": {
            "format": "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "complex",
            "level": "DEBUG",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "error.log",
            "formatter": "complex",
            "level": "ERROR",
        },
    },
    "root": {"handlers": ["console", "file"], "level": "WARNING"},
    "loggers": {"brief": {"level": "INFO"}, "detail": {"level": "DEBUG"}}
}


def config_logging():
    logging.config.dictConfig(__config)
