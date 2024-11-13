from logging import getLogger, StreamHandler, Formatter, DEBUG, FileHandler, WARNING, ERROR, CRITICAL, INFO


logger = getLogger()
# logger.setLevel(DEBUG)
# logger.setLevel(INFO)
# logger.setLevel(WARNING)
# logger.setLevel(ERROR)
logger.setLevel(CRITICAL)

formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.addHandler(StreamHandler())
logger.addHandler(FileHandler('exemplo.log'))

for handler in logger.handlers:
    handler.setFormatter(formatter)

logger.debug('Mensagem de debug')

logger.info('Mensagem de info')

logger.warning('Mensagem de warning')

logger.error('Mensagem de error')

logger.critical('Mensagem de critical')