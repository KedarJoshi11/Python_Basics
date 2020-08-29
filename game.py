# from random import randint
# random_number = randint(1, 10)

# while True:
# 	guess = int(input("Pick a number between 1 - 10: "))
# 	if guess > random_number:
# 		print("Too high")
# 	elif guess < random_number:
# 		print("Too Low")
# 	else:
# 		print("You won!")
# 		replay = input("Press \"Y\" to play again and \"N\" to quit: ")
# 		replay = replay.lower()
# 		if replay == 'y':
# 			random_number = randint(1, 10)
# 			guess = None
# 		elif replay == 'n':
# 			print("Thank You for playing!")
# 			break













#handle user guesses
#	if they guess correct, tell them they won
#		otherwise tell them if they are too high or too low. 

#bonus - let player play again if they want!


from random import randint
random_number = randint(1,10)
while True:
	guess = int(input("Pick a number between 1 - 10: "))
	if guess > random_number:
		print("Too High!")
	elif guess < random_number:
		print("Too Low")
	else: 
		print("You won!")
		print("Do you want to play again? Press \"Y\" for yes and \"N\" for no. ")
		replay = input()
		replay = replay.lower()
		if replay == 'y':
			guess = None
		else:
			print("Thank You for Playing!")
			break