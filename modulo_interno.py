# modulo_interno.py

from logzero import logger, logfile, setup_logger
import logging
import config_logzero as log


def funcion_en_modulo_interno():
    try:
        x=1/0
    except:
        return log.config_log().critical("error en modulo interno")
    