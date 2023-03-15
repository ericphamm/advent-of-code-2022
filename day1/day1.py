with open('day1/day1.txt') as file:
	content = file.read().strip().split("\n")

# print(content)

calories = 0
max = 0

for item in content:
	if item == '':
		calories = 0
	else:
		calories += int(item)
		if calories > max:
			max = calories

print(max)