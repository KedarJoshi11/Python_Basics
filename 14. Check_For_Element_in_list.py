squad = []
print("Enter the playing eleven: ")
while len(squad) < 11:
	p = input("Enter player name: ")
	squad.append(p)
	
#using list comprehension
squad = [x.title() for x in squad]

check = " "
while True:
	check = input("\nEnter the player you want to check for or enter \"Done\" to exit: ")
	check = check.title()
	if check == 'Done' or check == 'DONE' or check == 'done':
		break
	if check in squad:
		print(f"Yes, {check} will be playing. \n")
	else:
		print(f"{check} will not be playing. \n")

print("\nThe team sheet you selected is: ")
i=0
for p in squad:
	print(f"{i+1}: {p}")
	i += 1

