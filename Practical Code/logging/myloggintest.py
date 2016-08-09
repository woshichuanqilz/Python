import logging

# create logger with 'spam_application'
logger = logging.getLogger('spam_application')

# disable the logger
# logger.disabled = True

logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level, if you set the level to the info level the log will not be showed here.
ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)

ch.setLevel(logging.DEBUG)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


# info test 
# logger.warning('this is the lizhe\'s test')

FORMAT = '%(asctime)-15s %(levelname)s %(name)-8s %(message)s'
logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
logger = logging.getLogger('tcpserver')
logger.warning('Protocol problem: %s', 'this is lizhe test')


