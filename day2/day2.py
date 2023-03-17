with open('day2/day2.txt') as file:
	content = file.read().strip().split('\n')

# print(content)

# Part 1
combo = {
'A X' : 4,
'A Y': 8,
'A Z': 3,
'B X' : 1,
'B Y' : 5,
'B Z' : 9,
'C X' : 7,
'C Y' : 2,
'C Z' : 6
}

total = 0

for round in content:
	total = total + combo[round]

print(total)