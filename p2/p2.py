first = 1
second = 1
third = first + second
sum = 0
while third <= 4000000:
	sum += third
	first = second + third
	second = first + third
	third = first + second

print sum
