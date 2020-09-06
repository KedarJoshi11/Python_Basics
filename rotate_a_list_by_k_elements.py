l1 = []
a = None
k = None
#Function to capture lists
def capture_lists(l1):
	print("Enter \"done\" when list is compelete. ")
	while True:
		a = input("Enter element: ")
		if a == 'Done' or a == "done" or a == "DONE":
			break
		l1.append(int(a))
	return l1
#Function to rotate lists
def rotate_list(l1):
	res_list = []
	while True:
		k = input("Enter the number of elements you want to rotate the list by: ")
		if k.isdigit():
			while True:
				rot = input("Enter \"R\" for clock wise and \"L\" for anti-clock wise. ")
				if rot == "R" or rot == "r":
					res_list = l1[int(k):] + l1[:int(k)]
					break
				elif rot == "L" or rot == "l":
					k = int(k)
					res_list = l1[-k:] + l1[:-k]
					break
				else:
					print("Please only enter a valid input. ")
			break
		else:
			print("Only numbers are accepted. ")

	return res_list
#capturing a list from the user
capture_lists(l1)
print("The list you entered is: ")
print(l1)
#rotating the input list
print(f"The list after rotating by {k} is : {rotate_list(l1)}")


