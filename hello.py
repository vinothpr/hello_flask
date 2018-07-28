from flask import Flask
from flask import request
import logging
from logging.handlers import RotatingFileHandler
from flask import json
from time import strftime

app = Flask(__name__)
 
@app.route("/", methods = ['GET', 'POST'])
def hello():
    ts = strftime('[%Y-%b-%d %H:%M]')
    logger.info(ts + ' - ' + request.url)
    return_dict = {}
    return_dict['message'] = 'Good morning'
    response = app.response_class(response=json.dumps(return_dict), status=200, mimetype='application/json')
    if request.headers['Accept'] == 'application/json':
	return response 
    else:
        return "<p>Hello World!<p>"
 
if __name__ == "__main__":
    ts = strftime('[%Y-%b-%d %H:%M]')
    handler = RotatingFileHandler('hello.log', maxBytes=10000, backupCount=1)
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    app.run()
