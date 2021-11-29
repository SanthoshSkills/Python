import urllib.request, urllib.parse, urllib.error
import ssl
import json

api_key = False

if api_key == False:
    api_key = 42
    servicecurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    servicecurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1 :
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key

    url = servicecurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters')
    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print("====Failed to convert====")
        print(data)

    #print(json.dumps(js, indent=4))
    print(js['results'][0]['place_id'])
