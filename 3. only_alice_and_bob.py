name1 = 'alice'
name2 = 'bob'
name = input("What's your name?")
if(name.lower() == name1 or name.lower() == name2):
	print("Hey there, "+ name.capitalize() + ". How are you?")
else:
	print("You're not Alice or Bob. I am not allowed to greet you. ")