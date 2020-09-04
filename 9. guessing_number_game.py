from random import randint
guess = None
answer = randint(1, 10)
count = 0
print(answer)
while(guess != answer):
	guess = int(input("Guess a number between 1 - 10: "))
	count += 1
	if(guess > answer):
		print("Too high. ")
	elif(guess < answer):
		print("Too low")
	elif(guess == answer):
		print("Number of attempts it took you to win: " + str(count))


