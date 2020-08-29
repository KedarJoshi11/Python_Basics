def colorize(text, color):
	colors = ("Cyan", "Yellow", "Blue", "green", "magenta")
	if type(text) is not str:
		raise TypeError("Text must be instance of str")
	if color not in colors:
		raise VlueError("Color is invalid color") 
	print(f"Printed {text} in {color}")
	
colorize("hi", "chicken")
#colorize(5, "chicken")