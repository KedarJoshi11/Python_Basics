print("....Rock.....")
print("....Paper....")
print("...Scissors...")
print("SHOOT!!!!")
p1 = input("Player one choose: ")
p2 = input("Player two choose: ")
if (p1 == 'rock' or p1 == 'scissors' or p1 == 'paper') and (p2 == 'rock' or p2 == 'paper' or p2 == 'scissors'):
	if p1 == 'rock' and p2 == 'scissors':
		print("Rock beats scissors, player one Wins!")
	elif p1 == 'rock' and p2 == 'paper':
		print("Paper Beats rock, Player 2 wins!")
	elif p1 == 'rock' and p2 == 'rock':
		print("Game Draw!")
	elif p1 == 'paper' and p2 == 'scissors':
		print("Scissors beat paper, player 2 wins!")
	elif p1 == 'paper' and p2 == 'rock':
		print("Paper beats rock, Player 1 wins!")
	elif p1 == 'paper' and p2 == 'paper':
		print("Game Draw!")
	elif p1 == 'scissors' and p2 == 'rock':
		print("rock beats scissors, player 2 wins")
	elif p1 == 'scissors' and p2 == 'paper':
		print("Scissors beat paper, player 1 wins!")
	elif p1 == 'scissors' and p2 == 'scissors':
		print("Game draw")
else:
	print("Please pick your weapons from the arsenal available!")