import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

count = dict()
for line in fhand :
    print(line.decode().strip())
