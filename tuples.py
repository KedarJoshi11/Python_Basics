#Tuples are commonly used for unchanging data. 

months = ("January", "February", "March", "April", "March", "May", "June", "July", "August", "September", "October", "November", "December")


# Tuples can be used as keys in dictionaries. 

locations = {
	(35.6895, 39.6917): "Tokyo Office",
	(40.7128, 74.0060): "New York Office",
	(37.5666, 22.4194): "San Francisco"

}

# Some dictionary methods like .items() return tuples. 

cat = {"name": "biscut", "age": 0.5, "favourite_toy": "my chapstick"}
cat.items()

# >>> dict_items([('name', 'biscut'), ('age', 0.5), ('favorite_toy', 'my chapstick')])
                       # tuple ^        # tuple ^       # tuple ^

