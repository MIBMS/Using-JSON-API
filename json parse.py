import json
import urllib.request as req

url = input('Enter URL: ')

json_string = req.urlopen(url).read().decode()

js = json.loads(json_string)

##print(json.dumps(js, indent = 4))

sum_count = 0

for user in js["comments"]:
    sum_count += int(user["count"])

print(sum_count)
