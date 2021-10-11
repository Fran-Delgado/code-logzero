#import logger and logfile
from logzero import logger, logfile
import logging

#seteamos el fichero de salida y el nivel de log 
# En la consola aparecen todos los mensajes de todos los niveles de log, pero  en el fichero 
# de salida solo aparecen desde el nivel de log seleccionado en adelante según criticidad.

logfile('C:\\Users\\f.delgadomartinez\\Desktop\\INVENTOS PYTHON\\logzero\\my_logfile.log',
        loglevel=logging.WARNING,
        disableStderrLogger=True) # No se muestran mensajes en consola pero si se guardan en fichero.

# Log messages
# Si el fichero de log ya existe la información se añade.


logger.debug("Este mensaje se ve por consola pero no en el fichero de log (caso WARN)")
logger.info("Este mensaje se ve por consola pero no en el fichero de log (caso WARN)")
logger.warning("Este mensaje se ve por consola y en el fichero de log (caso WARN)")
logger.error("Este mensaje se ve por consola y en en el fichero de log (caso WARN)")
logger.critical("Este mensaje se ve por consola y en el fichero de log (caso WARN)")

