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
type1 = 0
type2 = 0
type3 = 0
type4 = 0
subject1 = 0
subject2 = 0
subject3 = 0
subject4 = 0
date1 = 0
date2 = 0
date3 = 0
date4 = 0
class application:

  def __init__(self, difficulty, subject , dueDate):
    self.subject = subject
    self.difficulty = difficulty
    self.dueDate = dueDate
    self.priority = difficulty - 4*dueDate
    
app = Flask(__name__)
applications = []
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
    type1 = parameters.get('type1')
    type2 = parameters.get('type2')
    type3 = parameters.get('type3')
    type4 = parameters.get('type4')
    subject1 = parameters.get('subject1')
    subject2 = parameters.get('subject2')
    subject3 = parameters.get('subject3')
    subject4 = parameters.get('subject4')
    date1 = parameters.get('date1')
    date2 = parameters.get('date2')
    date3 = parameters.get('date3')
    date4 = parameters.get('date4')
        
    
   
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')

applications.append(application(type1, subject1, date1)) 
applications.append(application(type2, subject2, date2)) 
applications.append(application(type3, subject3, date3)) 
applications.append(application(type4, subject4, date4)) 

def insertion_sort():
  for i in range(1,len(applications)):
    number = applications[i].priority
    newthing = applications[i]
    othernum = i
    shift_position = i - 1
    while shift_position >= 0:
      if number < applications[shift_position].priority:
        applications[othernum] = applications[shift_position]
        applications[shift_position] = newthing
        shift_position = shift_position - 1
        othernum = othernum - 1
      else:
        break


insertion_sort()
block1 = applications[0].subject
block2 = applications[1].subject
block3 = applications[2].subject
block4 = applications[3].subject
print(block1)

import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

def main2():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main2()
