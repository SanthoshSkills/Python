import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
print("Retrieving",url)
html = urllib.request.urlopen(url, context = ctx)
data = html.read().decode()
print("Retrieved",len(data),"characters")
try:
    js = json.loads(data)
except:
    js = None

if js is None:
    print("====Failed to retrieve====")
    print(data)
    quit()
#print(js)
x=0
cnt=0
print("Count:",len(js["comments"]))
#print(json.dumps(js, indent=4))
for cnt in range(len(js["comments"])) :
    x = x + js["comments"][cnt]['count']
print("Sum:",x)
