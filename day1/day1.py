with open('day1/day1.txt') as file:
	content = file.read().strip().split("\n")

# print(content)
# Part1
calories = 0
max = 0

for item in content:
	if item == '':
		calories = 0
	else:
		calories += int(item)
		if calories > max:
			max = calories

# Part 1 answer
print(max)

#Part2
calories2 = 0
max1 = 0
max2 = 0
max3 = 0

for item in content:
	if item == '':
		calories2 = 0
	else:
		calories2 += int(item)

		if calories2 > max3:
			max3 = calories2
		elif calories2 > max2:
			max2 = calories2
		elif calories2 > max1:
			max1 = calories2

print(max3)
print(max2)
print(max1)