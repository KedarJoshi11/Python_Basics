print("Enter numbers you want to add or enter \"done\" when you want to stop. ")
list1 = []
a = None

while True:
	a = input("Enter number: ")
	if a == 'done':
		break
	list1.append(a)

def sum_using_for(list1):
	total = 0
	for n in list1:
		total = total + int(n)
	return total

def sum_using_while(list1):
	total = 0
	i = 0
	while i < len(list1):
		total = total + int(list1[i])
		i += 1
	return total

def sum_using_recursion(list1):
	if len(list1) == 0:
		return 0
	else:
		return int(list1[0]) + sum_using_recursion(list1[1:])

print(f"sum using for loop: {sum_using_for(list1)}\n")
print(f"sum using while loop: {sum_using_while(list1)}\n")
print(f"sum using recursion: {sum_using_recursion(list1)}\n")

