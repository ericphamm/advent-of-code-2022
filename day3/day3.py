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
	# print(first_compar,"\n",second_compar)

	for priority,character in enumerate(ascii_letters):
		if character in first_compar and character in second_compar:
			total_priority = total_priority + priority

print(total_priority)
