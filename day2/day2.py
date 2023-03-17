with open('day2/day2.txt') as file:
	content = file.read().strip().split('\n')

# print(content)

# Part 1

#A Rock, B Paper, C Scissors
#X for Rock, Y for Paper, and Z for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won

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

# Part 2

#A Rock, B Paper, C Scissors
#X lose, Y draw, Z win
#1 for Rock, 2 for Paper, and 3 for Scissors
#0 if you lost, 3 if the round was a draw, and 6 if you won

combo_2 = {
'A X' : 0 + 3,
'A Y': 3 + 1,
'A Z': 6 + 2,
'B X' : 0 + 1,
'B Y' : 3 + 2,
'B Z' : 6 + 3,
'C X' : 0 + 2,
'C Y' : 3 + 3,
'C Z' : 6 + 1
}

total2 = 0

for round in content:
	total2 = total2 + combo_2[round]

print(total2)