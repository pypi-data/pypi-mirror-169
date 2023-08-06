import sys
import logging
from venv import create


class Logs_Manager():
    def __init__(self, log_name, log_level):
        self.log_name = log_name
        self.log_level = log_level
        return self.create_logger()

    def create_logger(self):
        logger = logging.getLogger(self.log_name)

        if self.log_level == 'info':
            logger.setLevel(logging.INFO)  

        elif self.log_level == 'warning':
            logger.setLevel(logging.WARNING)  

        elif self.log_level == 'debug':
            logger.setLevel(logging.DEBUG)  

        else:
            logger.setLevel(logging.INFO)  
            
        formatter = logging.Formatter(  
            '%(levelname)s:%(module)s:%(message)s')
        
        handler = logging.StreamHandler(sys.stderr)
        
        handler.setFormatter(formatter)
        logger.addHandler(handler) 
        _logger = logging.LoggerAdapter(logging.getLogger(self.log_name)) 
        return _logger


