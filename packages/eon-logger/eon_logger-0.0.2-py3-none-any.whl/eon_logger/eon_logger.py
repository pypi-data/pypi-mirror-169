import sys
import logging

def LoggerCreator(log_name, log_level):
    logger = logging.getLogger(log_name)

    if log_level == 'info':
        logger.setLevel(logging.INFO)  

    if log_level == 'warning':
        logger.setLevel(logging.WARNING)  

    if log_level == 'debug':
        logger.setLevel(logging.DEBUG)  
        
    formatter = logging.Formatter(  
        '%(levelname)s:%(module)s:%(message)s')
    
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.INFO)
    
    handler.setFormatter(formatter)
    logger.addHandler(handler) 
    _logger = logging.LoggerAdapter(logging.getLogger(log_name)) 
    return _logger