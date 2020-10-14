def count_rows():
	f = open(str(file), "r")
	rows = 0
	data = f.read()
	lines = data.split("\n")

	for l in lines:
		if l:
			rows += 1
	f.close()
	return rows

def count_columns():
	r = []
	f = open(str(file), "r")
	for i in f:
		line = i.split()
		num = len(line)
		r.append(num)
	f.close()
	columns = max(r)
	return columns

while True:
	try: 
		operator, file = input("Enter your query as {numrows/numcols textfile.txt}: ").split()
		operator = operator.lower()
		if operator == 'exit':
			break
		elif operator == 'numrows':
			print(f"The number of rows in textfile = {count_rows()}")
		
		elif operator == 'numcols':
			print(f"The number of columns in text file are = {count_columns()}")

		else:
			print("Wrong input, please try again.")
	
	except ValueError:
		d = input("Enter \"Y\" to confirm quitting or any other input to continue using the program. ")
		d = d.lower()
		if d == "y":
			break
		else:
			pass

	except FileNotFoundError:
		print("The file doesn't exist, please use a valid file. ")
		
		




