from random import randint

def fnGetDice():
	while 1:
		# get number of Dice
		try:
			dice = int(input("""How Many dice will you roll? (1-10)
			"""))
			return dice
			break
		except ValueError:
			print("Please enter a valid number")

def fnGetSides():
	while 1:
		#get number of sides on dice
		try:
			if dice == 1:
				sides = int(input("""How Many sides will it have? (2-20)
				"""))
			else:
				sides = int(input("""How Many sides will they have? (2-20)
				"""))
			return sides
			break
		except ValueError:
			print("Please enter a valid number")

repeat = 1;	#state of main loop

#main loop
while repeat:

	#dice loop
	dice = 0
	invalid_dice = 1
	while invalid_dice:

		dice = fnGetDice()

		if (dice > 0) and (dice < 11):
			invalid_dice = 0
		else:
			invalid_dice = 1
			print("Please enter a valid number")

	#sides loop
	sides = 0
	invalid_sides = 1
	while invalid_sides:

		sides = fnGetSides()
		if (sides > 1) and (sides < 21):
			if dice == 1:
				print("***Rolling ",dice," ",sides, "sided die")
			else:
				print("***Rolling ",dice," ",sides, "sided dice")
			invalid_sides = 0
		else:
			invalid_dice = 1
			print("Please enter a valid number")

	# var for counting
	total = 0		#total of rolls
	roll_count = 0	# num of rolls and min possible from rolls
	max_count = 0	# max possible from rolls

	# dice rolling loop
	while dice:

		# get random number
		rnd = randint(1,sides)
		print("-Roll_", roll_count, " = ", rnd)

		# update the total of the rolls
		total = total + rnd

		# update min, max and reduce left to roll
		roll_count += 1		#min
		max_count = max_count + sides	#max
		dice -= 1

	# out of loop
	#Check if you rolled min or max
	if(total == roll_count):	# min
		print("\nYou suck!  You rolled", total)
	elif(total == max_count):	# max
		print("\nYou the man!  You rolled", total)
	else:
		print("\nRoll total = ", total)

	print("\n\nmin total = ", roll_count)
	print("max total = ", max_count)

	# prompt to roll again
	if ("y" or "yes") in input("\nagain? ").lower():
		repeat = 1
	else:
		repeat = 0
