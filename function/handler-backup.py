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
    
    req_json = req.get_json(force=True, silent=True, cache=True)
    if not req_json:
        log.debug('Request could not be processed. Json formatted data not vailable...')
        return 'Could not process data. Json formatted data not vailable...'
        
    #convert the json representation into a python object
    json_req = json.loads(req_json, strict=False)
    #requests.data contains the json in string format, so you can process the characters that needs to be escaped.
    #json_req = json.loads(request.data, strict=False)
    
    # extract key and value
    result = {"key": json_req["key"], "value": json_req["value"]}
    
    # Serialize to a JSON formatted string 
    str_rep = json.dumps(result)
    received_data = str_rep
    log.debug('Received Message: ' + str_rep)
    #resp = Response(str_rep, status=200, mimetype='application/json')
    #return resp
    #received_data = str(req.get_data(cache=True, as_text=True, parse_form_data=False))
    
    #raw_data = req.get_data(parse_form_data=False)
    
    #try:
        #received_data = str(raw_data.decode("utf-8"))
    #except ValueError as e:
         #return 'Could not parse data...'
        
    #log.debug('Data: ' + received_data)
    #log.debug('Dict: ' + str(req.__dict__))

    return 'Received Message: ' + received_data
    #return 'Received Message: ' + str_rep
