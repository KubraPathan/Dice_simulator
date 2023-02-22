import random


again = True

while again:
	
	# Generates a random number
	# between 1 and 6 (including
	# both 1 and 6)
	no = random.randint(1,6)
	print(no)
	another_roll = input("Want to roll the dice again?(y/n):")
	if another_roll.lower()=="y":
		continue
	else:
		break
	
	
