import json
from flask import Response
import logging
import time

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    
    #log.debug('Data: ' + received_data)
    log.debug('Dict: ' + str(req.data))
    log.debug('Sleeping for 25 miliseonds!.')
    time.sleep(0.025)
    log.debug( 'Sleeping completed.')

    return 'Received Message: ' + str(req.data)
 
