import re

hand = open('regex_sum_280224.txt','r')

for line in hand:
	line = line.rstrip()
	nums = re.findall('[0-9]+', line)
	if not nums: continue
	print nums
