favorite_movies = ["Power", "Ted", "The notebook", "The pursuit of happyness", "Me before you"]
print(f"The list favorite movies includes my top{len(favorite_movies)} favorite movies")
print(favorite_movies)   

print(sorted(favorite_movies)) # sorted gave me a list with alphabetically orderd
print(favorite_movies)         # As listed at first

favorite_movies.sort()
print(favorite_movies)

favorite_movies.append("A walk to remember")
favorite_movies.append("Titanic")
print(f"I added two more favorite movies on my favorite movies list {favorite_movies}")
