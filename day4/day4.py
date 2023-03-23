with open('day4/day4.txt') as file:
	content = file.readlines()

# print(content)
total = 0
for pairs in content:
	section = pairs.split(",")

	first_elf = (section[0].split("-"))
	second_elf = section[1].split("-")
	if (int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1])) or (int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1])):
		total += 1

print(total)