#Using the GeoJSON API

import urllib.request, urllib.parse, urllib.error
import json


serviceurl = 'http://py4e-data.dr-chuck.net/json?'


address = input('Enter location: ') #Gauhati University

url = serviceurl + urllib.parse.urlencode({'address':address,'key':42})
print ('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()
print ('Retrieved',len(data),'characters')

js = json.loads(data)

print ('The place ID is:', js['results'][0]['place_id'])