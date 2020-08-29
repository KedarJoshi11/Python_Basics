from random import randint
player_wins = 0
computer_wins = 0
goal = 3
while player_wins < goal and computer_wins < goal:
	print(f"Player Score: {player_wins}			                                              Computer Score: {computer_wins}")
	print(".....................................................Rock.........................................................")
	print(".................................................... Paper........................................................")
	print("....................................................Scissors......................................................")
	print("....................................................SHOOT!!!!.....................................................")
	print("\n")
	player = input("Player, make your move or press q to quit:  ").lower()
	if player == 'quit' or player == 'q':
		break
	rand_num = randint(0,2)
	if rand_num == 0:
		computer = 'rock'
	elif rand_num == 1:
		computer = 'paper'
	else:
		computer = 'scissors'
	print(f"Computer plays: {computer}")
	if player == computer:
		print("It's a tie!")
		print("\n")
	elif player == 'rock':
		if computer == 'scissors':
			print("You win!")
			print("\n")
			player_wins += 1
		else:
			print("Computer wins!")
			print("\n")
			computer_wins += 1
	elif player == 'paper':
		if computer == 'rock':
			print("You win!")
			print("\n")
			player_wins += 1
		else:
			print("Computer wins!")
			print("\n")
			computer_wins += 1
	elif player == 'scissors':
		if computer == 'paper':
			print("You win!")
			print("\n")
			player_wins += 1
		else:
			print("Computer wins!")
			print("\n")
			computer_wins += 1
	else:
		print("Please don't use any weapons other than rock, paper or scissors. ")
if player_wins > computer_wins:
	print("Congrats, you won the match!")
	print("Final Score:.......................................")
	print(f"Player:   {player_wins}")
	print(f"Computer: {computer_wins}")
	print("\n")
	print("Thank you for playing!")
elif player_wins < computer_wins:
	print("Computer Won the match :(")
	print("Final Score:.......................................")
	print(f"Player:   {player_wins}")
	print(f"Computer: {computer_wins}")
	print("\n")
	print("Thank you for playing!")
elif player_wins == computer_wins:
	print("Game draw!")
	print("Final Score:.......................................")
	print(f"Player:   {player_wins}")
	print(f"Computer: {computer_wins}")
	print("\n")
	print("Thank you for playing!")
