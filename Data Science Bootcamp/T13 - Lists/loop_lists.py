'''
create list variable with 5 movies
fav_movies = [list 5 movies]
create while loop to print out all movies in the format: Movie: {fav_movies}
for i in range(len(fav_movies)):
	print(f"Movie: {fav_movies[i]}")

'''

fav_movies = ['Spiderman', 'Superman', 'Ironman', 'Doctor Strange', 'Captain America']

for i, movie in enumerate(fav_movies, start=1): #for every movie print movie number and the corresponding movie name 
     print(f"Movie {i}: {movie}")
# looked up enumerate - definitely cleaner than not using it - code without enumerate below 
'''
this is the way I did it originally

for i in range(len(fav_movies))
	print(f"Movie {i+1}: {fav_movies[i]}")
'''