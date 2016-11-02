import urllib
import re
from BeautifulSoup import *

html = urllib.urlopen('http://python-data.dr-chuck.net/comments_280229.html').read()

soup = BeautifulSoup(html)

sum = 0

tags = soup('span')
for tag in tags:
	line = str(tag)
	nums = re.findall('[0-9]+', line)
	if len(nums) > 0:
		for num in nums:
			sum += int(num)
print sum
