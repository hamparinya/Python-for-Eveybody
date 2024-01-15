from os import path
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter location:') #http://py4e-data.dr-chuck.net/comments_1002556.xml
html = urllib.request.urlopen(link).read().decode()
print('retrieved',link)
print("retrieved",len(html), 'characters')

# calculation
count = 0
sum = 0
data = ET.fromstring(html)
tags = data.findall('comments/comment')
for tag in tags:
    count = count + 1
    sum = sum + int(tag.find('count').text)

print('Count:', count)
print('Sum :', sum)
