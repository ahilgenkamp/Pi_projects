# Attempt at a Monopoly simulation

# load packages
from random import randint


# random dice roll
def roll_dice():
	d1 = randint(1, 6)
	d2 = randint(1, 6)
	return (d1, d2)

for n in range(0,10):
	roll = roll_dice()
	if roll[0] == roll[1]:
		print(str(roll) + ' Doubles!!')
	else:
		print(str(roll))


#Chance Cards


#Community Chest


#Bank Money
