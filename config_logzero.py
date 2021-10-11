# config_logzero.py

from logzero import logger, logfile, setup_logger
import logging

def config_log():
    my_formatter = logging.Formatter('%(filename)s - %(asctime)s - %(levelname)s: %(message)s');

    #create custom logger instance
    custom_logger = setup_logger(
    name="My Custom Logger",
    logfile="C:\\Users\\f.delgadomartinez\\Desktop\\INVENTOS PYTHON\\logzero\\my_logfile_2.log",
    formatter=my_formatter,
    maxBytes=1000000,
    backupCount=3,level=logging.INFO)
    # json=True)
    # disableStderrLogger=True)

    return custom_logger
