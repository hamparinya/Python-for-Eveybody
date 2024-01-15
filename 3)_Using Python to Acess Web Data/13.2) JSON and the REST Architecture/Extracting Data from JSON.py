import urllib.request, urllib.parse, urllib.error
import json

link = input('Enter location:') #http://py4e-data.dr-chuck.net/comments_1002557.json
print('Retrieving: ', link)
data = urllib.request.urlopen(link).read().decode()
print('Retrived', len(data),'characters')

infol = json.loads(data)
add = 0
sum = 0
for item in infol['comments']:
    sum += int(item['count'])
    add += 1

print("Count: ", add)
print("Sum", sum)
 


'''$ python3 solution.py
Enter location: http://py4e-data.dr-chuck.net/comments_42.json
Retrieving http://py4e-data.dr-chuck.net/comments_42.json
Retrieved 2733 characters
Count: 50
Sum: 2...'''