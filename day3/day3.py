from string import ascii_letters

with open('day3/day3.txt') as file:
	content = file.read().strip().split("\n")

# print(content)

# First part
total_priority = 0

for items in content:

	half_items = len(items)//2

	first_compar = set(items[:half_items])
	second_compar = set(items[half_items:])

	for priority,character in enumerate(ascii_letters):
		if character in first_compar and character in second_compar:
			total_priority = total_priority + priority + 1 #because priority starts with a = 1

print(total_priority)

# Second part
total_priority2 = 0

j = 3
for i in range(0, len(content), 3):
	each_group = content[i:j]
	j += 3

	for priority, character in enumerate(ascii_letters):
		if character in each_group[0] and character in each_group[1] and character in each_group[2]:
			total_priority2 = total_priority2 + priority

print(total_priority2)
