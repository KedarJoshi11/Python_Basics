import random
random_number = random.randint(1,10) #numbers 1 - 10 (Randint is inclusive, ranges are exclusive. Something to keep your brain active)
#handle user guesses
#	if they guess correct, tell them they won
#		otherwise tell them if they are too high or too low. 

#bonus - let player play again if they want!
guess = None
while guess != random_number:
	guess = int(input("Pick a number between 1 - 10: "))
	if guess > random_number:
		print("Too High!")
	elif guess < random_number:
		print("Too Low!")
	else:
		print("You won!")
print("\n")
print("This was fun, do you want to play again? Press \"Y\" for yes and \"N\" for no")
replay = str(input())
replay = replay.lower()
while replay == 'y':
	guess = None
	while guess != random_number:
		guess = int(input("Pick a number between 1 - 10: "))
		if guess > random_number:
			print("Too High!")
		elif guess < random_number:
			print("Too Low!")
		else:
			print("You won!")
			random_number = random.randint(1,10)
			print("Do you want to play again? Press \"Y\" for yes and \"N\" for no")
			replay = str(input())
			replay = replay.lower()
if replay == 'n':
	exit()





