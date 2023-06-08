from pydantic import BaseModel
import os


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "influxDB_crud"
    if not os.path.isdir("./logs"):
        os.mkdir("./logs")
    LOG_FORMAT: str = (
        '{"time": "%(asctime)s", "level": "%(levelname)s", '
        + '"thread": "%(threadName)s", "component": "%(module)s",'
        + f'"service": "{LOGGER_NAME}", "payload": %(message)s}}'
    )
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "DEBUG")

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "class": "uvicorn.logging.DefaultFormatter",
            "format": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": LOG_LEVEL,
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "level": LOG_LEVEL,
            "filename": f"./logs/{LOGGER_NAME}.log",
            "mode": "a",
            "encoding": "utf-8",
            "maxBytes": 500000,
            "backupCount": 4,
        },
    }
    loggers = {
        "root": {
            "handlers": ["console", "file"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    }