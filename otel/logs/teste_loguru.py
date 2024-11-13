from loguru import logger
from sys import stdout

logger.add(stdout, level='DEBUG', serialize=True)

logger.add('loguru.log', level='DEBUG', serialize=True)


logger.debug('Mensagem de debug')