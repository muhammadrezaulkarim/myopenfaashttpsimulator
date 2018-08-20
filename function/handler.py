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
    #convert the json representation into a python object
    #json_req = json.loads(req)
    
    # extract key and value
    #result = {"key": json_req["key"], "value": json_req["value"]}
    
    # serialize to a JSON formatted string 
    #str_rep = json.dumps(result)
    #log.debug('Received Message: ' + str_rep)
    #resp = Response(str_rep, status=200, mimetype='application/json')
    #return resp
    
    log.debug('Received Message: ' + str(req))

    return  'Received Message: ' + str(req)
