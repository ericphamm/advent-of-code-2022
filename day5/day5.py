with open('day5/day5.txt') as file:
	stacks, instructions = (i.splitlines() for i in file.read().split("\n\n"))

print(stacks, instructions)

