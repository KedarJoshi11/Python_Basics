print("This program will add all the numbers you put in. ")
print("\nEnter \"done\" whenever you want to close the program. ")

numbers = []
total = 0
count = 0

while True:
	a = input("Enter number: ")
	a.lower()
	if a == 'done':
		break
	total += int(a)
	count += 1
	print(f"Sum = {total}")

print(f"\nYou added a {count} numbers. Total Sum = {total}\n")
