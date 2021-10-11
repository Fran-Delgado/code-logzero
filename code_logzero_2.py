# code_logzero.py

from logzero import logger, logfile, setup_logger
import logging
import config_logzero as log
import modulo_interno

# Log messages
log.config_log().info("This log message saved in the log file")
log.config_log().warning("This log message saved in the log file")

modulo_interno.funcion_en_modulo_interno()