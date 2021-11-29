# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
'''
Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
Find the link at position 3 (the first name is 1). Follow that link. Repeat this process 4 times. The answer is the last name that you retrieve.
Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
Last name in sequence: Anayah
Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Ardal.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.
Hint: The first character of the name of the last page that you will load is: S
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - URL: ')
position = input('Enter - position: ')
try:
    position = int(position)
except:
    print('Please enter a number')
    quit()
count = input('Enter - count: ')
try:
    count = int(count)
except:
    print('Please enter a number')
    quit()
if position <= 0 or count <= 0 :
    print('Enter positive numbers for position and count')
    quit()
else:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    print('Retrieving: ', url)

    # Retrieve specific anchor tag
    for i in range(int(count)):
        tags = soup('a')
        tagsinfile = list()
        for tag in tags:
        #print(tag.get('href', None))
            tagsinfile.append(tag.get('href', None))
        url = tagsinfile[position-1]
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        print('Retrieving: ',url)
    print('Final Answer: ',url)
