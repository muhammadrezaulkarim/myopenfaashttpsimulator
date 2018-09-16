import json
from flask import Response
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    
    #log.debug('Data: ' + received_data)
    log.debug('Dict: ' + str(req.data))

    return 'Received Message: ' + str(req.data)
 
