# the 6 models of Logging are : NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL

import logging 
logging.basicConfig(filename="logging.log", level= logging.DEBUG, format= '%(asctime)s %(message)s')
logging.info("THIS IS MY INFO LOGGING")
logging.error("this is my error message")
logging.critical("this is my critical")
logging.shutdown
