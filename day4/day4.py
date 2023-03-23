with open('day4/day4.txt') as file:
	content = file.readlines()

# Part 1
total = 0
for pairs in content:
	section = pairs.split(",") #['38-41','38-38']
	first_elf = (section[0].split("-")) #[38-41]
	second_elf = section[1].split("-") #[38-38]
	if (int(first_elf[0]) >= int(second_elf[0]) and int(first_elf[1]) <= int(second_elf[1])) or (int(first_elf[0]) <= int(second_elf[0]) and int(first_elf[1]) >= int(second_elf[1])):
		total += 1

print(total)