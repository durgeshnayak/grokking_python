import logging

logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.critical('EPIC SHIT HAPPENS')
logger.error('SHIT HAPPENS')
logger.warning('SHIT MIGHT HAPPEN')
logger.info('SHIT CAN HAPPEN')
logger.debug('SHIT SHIT SHIT')


