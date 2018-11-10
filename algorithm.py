from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template


# Flask app should start in global layout

app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    #print('Request:')
    #print(json.dumps(req, indent=4))
    res = processRequest(req)
    res = json.dumps(res, indent=4)
    print(res)

    # Extract current fcast
    # curr_fcast = res['query']['results']['channel']['item']['forecast']
    # curr_fcast_text = curr_fcast['text']
    
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    if req.get('result').get('action') == 'water-recommendation':
        result = req.get('result')
        parameters = result.get('parameters')
        #print(json.dumps(parameters, indent=4))
        baseurl = 'https://query.yahooapis.com/v1/public/yql?'
        yql_query = makeYqlQuery(req)
        if yql_query is None:
            return {}
        yql_url = baseurl + urlencode({'q': yql_query}) + '&format=json'
        result = urlopen(yql_url).read()
        data = json.loads(result)
        #print(data)
        res = makeWebhookResult(data, parameters)
    return res


def makeYqlQuery(req):
    result = req.get('result')
    parameters = result.get('parameters')
    city = parameters.get('geo-city')
    if city is None:
        return None
    #print(city)
    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" \
        + city + "')"


def makeWebhookResult(data, parameters):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    #print(json.dumps(parameters, indent=4))
    if result is None:
        return {'speech': 'No Result', 'displayText': 'No Result',
                'source': 'apiai-weather-webhook-sample'}
    channel = result.get('channel')
    if channel is None:
        return {'speech': 'No Channel', 'displayText': 'No Channel',
                'source': 'apiai-weather-webhook-sample'}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if location is None or item is None or units is None:
        return {'speech': 'No location or item or units',
                'displayText': 'No location or item or units',
                'source': 'apiai-weather-webhook-sample'}

    condition = item.get('condition')
    if condition is not None:
        for i in range(4) :
            assignments[i] = assignment(parameters.get('type' + str(i+1)), parameters.get('subject' + str(i+1)), parameters.get('date' + str(i+1))
            #assignments[i].difficulty = parameters.get('type' + str(i+1))   #Value between 0-4 (0 being worksheet, 4 being large project)
            #assignments[i].subject = parameters.get('subject' + str(i+1))   #Spanish, Science, Math, Social Studies, ELA
            #assignments[i].dueDate = parameters.get('due-date' + str(i+1))  #Value of FinalDate - Today's date
             
        #decision = ' need '
        
        return{}
        
        
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

class assignment:

  def __init__(self, difficulty, subject , dueDate):
    self.subject = subject
    self.difficulty = difficulty
    self.dueDate = dueDate
    self.priority = difficulty - 4*dueDate

def insertion_sort():
  for i in range(1,len(assignments)):
    number = assignments[i].priority
    newthing = assignments[i]
    othernum = i
    shift_position = i - 1
    while shift_position >= 0:
      if number < assignments[shift_position].priority:
        assignments[othernum] = assignments[shift_position]
        assignments[shift_position] = newthing
        shift_position = shift_position - 1
        othernum = othernum - 1
      else:
        break


insertion_sort()
block1 = assignments[0].subject
block2 = assignments[1].subject
block3 = assignments[2].subject
block4 = assignments[3].subject

response = json.loads(request.getresponse().read().decode('utf-8'))
message = response['result']['fulfillment']['speech']
print ("We're working on a thing")
