import re

hand = open('regex_sum_280224.txt','r')
sum = 0

for line in hand:
	line = line.rstrip()
	nums = re.findall('[0-9]+', line)
	if len(nums) > 0:
		for num in nums:
			sum = sum + int(num)
print sum
