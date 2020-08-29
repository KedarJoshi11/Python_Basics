playlist = {
	'title': 'Perspective',
	'author': 'Colt Steele',
	'songs': [
		{'title': 'song1', 'artist': ['Blue'], 'duration': 2.5},
		{'title': 'song2', 'artist': ['Kitty', 'djcat'], 'duration': 5.25},
		{'title': 'MeowMeow', 'artist': ['Garfield'], 'duration': 2.0},
	]
}

total_length = 0
for song in  playlist['songs']:
	total_length += song['duration']

print(total_length)
	