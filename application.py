
import urllib
import json
import os
omkomkokomko
from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "yahooWeatherForecast":
        return {}
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = makeYqlQuery(req)
    if yql_query is None:
        return {}
    yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
    print(yql_url)

    result = urllib.urlopen(yql_url).read()
    print("yql result: ")
    print(result)

    data = json.loads(result)
    res = makeWebhookResult(data)
    return res


def makeYqlQuery(req):
    parameters = result.get("parameters")


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}
    
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

try:
  import argparse
  flags = argparse.ArgumentParser(parents = [tools.argparser]).parse_args
except ImportError:
  flags = None
  
SCOPES = 'https://www.googleapis.com/auth/calendar'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
  creds = tools.run_flow(flow, store, flags) \
      if flags else tools.run(flow, store)
CAL = build('calendar', 'v3', http = creds.authorize(HTTP()))


now = str(datetime.datetime.today()).split()[0]
EVENT = {
  'summary': block1 + " homework",
  'start': {'dateTime': (now + 'T04:00:00%s')},
  'end': {'dateTime': (now + 'T05:00:00%s')},
}
EVENT2 = {
  'summary': block2 + " homework",
  'start': {'dateTime': (now + 'T05:00:00%s')},
  'end': {'dateTime': (now + 'T06:00:00%s')},
}
EVENT3 = {
  'summary': block3 + " homework",
  'start': {'dateTime': (now + 'T06:00:00%s')},
  'end': {'dateTime': (now + 'T07:00:00%s')},
}
EVENT4 = {
  'summary': block4 + " homework",
  'start': {'dateTime': (now + 'T07:00:00%s')},
  'end': {'dateTime': (now + 'T08:00:00%s')},
}
e = CAL.events().insert(calendarId = 'primary', sendNotifications = True, body = EVENT).execute()
e = CAL.events().insert(calendarId = 'primary', sendNotifications = True, body = EVENT2).execute()
e = CAL.events().insert(calendarId = 'primary', sendNotifications = True, body = EVENT3).execute()
e = CAL.events().insert(calendarId = 'primary', sendNotifications = True, body = EVENT4).execute()

import os.path
import sys

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai

CLIENT_ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'


def main3():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()

    request.lang = 'de'  # optional, default value equal 'en'

    request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

    request.query = "Hello"

    response = request.getresponse()

    print (response.read())
  
if __name__ == '__main__':
    main3()
