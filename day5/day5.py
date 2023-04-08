with open('day5/day5.txt') as file:
	stacks_strings, instructions = (i.splitlines() for i in file.read().split("\n\n"))

stacks = {int(digit):[] for digit in stacks_strings[-1].replace(" ","")}
# print(stacks, instructions)

def displayStacks():
	print("\n\nStacks:\n")
	for stack in stacks:
		print(stack, stacks[stack])
	print("\n")

displayStacks()
