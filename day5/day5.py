with open('day5/day5.txt') as file:
	stacks_strings, instructions = (i.splitlines() for i in file.read().split("\n\n"))

stacks = {int(digit):[] for digit in stacks_strings[-1].replace(" ","")}
# print(stacks, instructions)
indexes = [index for index, char in enumerate(stacks_strings[-1]) if char != " "]

def displayStacks():
	print("\n\nStacks:\n")
	for stack in stacks:
		print(stack, stacks[stack])
	print("\n")

def loadStack():
	for string in stacks_strings[:-1]:
		stack_num = 1
		for index in indexes:
			if string[index] != " ":
				stacks[stack_num].insert(0, string[index])
			stack_num += 1

loadStack()
displayStacks()