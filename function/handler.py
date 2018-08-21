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
    #req_json=req.get_json(force=True, silent=False, cache=True)
    #convert the json representation into a python object
    #json_req = json.loads(req_json)
    
    # extract key and value
    #result = {"key": json_req["key"], "value": json_req["value"]}
    
    # serialize to a JSON formatted string 
    #str_rep = json.dumps(result)
    #log.debug('Received Message: ' + str_rep)
    #resp = Response(str_rep, status=200, mimetype='application/json')
    #return resp
    #received_data = str(req.get_data(cache=True, as_text=True, parse_form_data=False))
    raw_data = request.get_data()
    
    try:
        received_data = str(raw_data.decode("utf-8"))
    except ValueError as e:
         return 'Could not parse data...'
        
    log.debug('Data: ' + received_data)
    log.debug('Dict: ' + str(req.__dict__))

    return 'Received Message: ' + received_data
    #return 'Received Message: ' + str_rep
