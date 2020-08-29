print("....Rock.....")
print("....Paper....")
print("...Scissors...")
print("SHOOT!!!!")
p1 = input("Player one choose: ")
print("No Cheating\n" * 100)
p2 = input("Player two choose: ")
if (p1 == 'rock' or p1 == 'scissors' or p1 == 'paper') and (p2 == 'rock' or p2 == 'paper' or p2 == 'scissors'):
	if p1 == p2:
		print("It's a tie!")
	elif p1 == 'rock':
		if p2 == 'scissors':
			print("Player 1 wins!")
		elif p2 == 'paper':
			print("Player 2 wins!")
	elif p1 == 'paper':
		if p2 == 'rock':
			print("Player 1 wins!")
		elif p2 == 'scissors':
			print("Player 2 wins!")
	elif p1 == 'scissors':
		if p2 == 'paper':
			print("Player 1 wins!")
		if p2 == 'rock':
			print("Player 2 wins!")
else:
	print("Please don't use any weapons other than rock, paper or scissors. ")

