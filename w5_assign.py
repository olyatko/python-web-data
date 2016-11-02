import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter location: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
tree = ET.fromstring(data)

counts = tree.findall('.//count')
sum = 0

for count in counts:
    nums = count.text
    nums = int(nums)
    sum += nums

print sum
