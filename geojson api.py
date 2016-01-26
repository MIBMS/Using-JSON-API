import urllib.request as req
import urllib.parse as par
import json

baseurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
address = input('Enter location: ')

url = baseurl + par.urlencode({'sensor':'false', 'address': address})

print("Retrieving " + url)

json_string = req.urlopen(url).read().decode()

js = json.loads(json_string)

#print(json.dumps(js, indent = 4))

place_id = js["results"][0]["place_id"]

print(place_id)

