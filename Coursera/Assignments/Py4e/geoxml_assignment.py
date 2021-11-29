import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL:')
print('Retrieving: ', url)
html = urllib.request.urlopen(url,context = ctx).read()
print("Retrieved: ", len(html), "characters")
#print(html.decode())
tree = ET.fromstring(html)
#print('Done decoded printing')
counts = tree.findall('comments/comment/count')
print('Count: ',len(counts), "comments")
x=0
for cnt in counts:
    x=x+int(cnt.text)
print("Sum of counts: ",x)
