"""
Top X movies from file - Simon King
"""

def initialise_list():
    filename = r"C:\labs\top250_movies.txt"
    movie_list = []
    with open (filename, mode="rt") as fh_in :
        for line in fh_in:
            movie_list.append(line[:-1])
    return movie_list

great_movies=initialise_list()
qty=int(input("How many movies would you like to see?"))
short_list = great_movies[:qty]
i=0
while i <len(short_list):
    print(short_list[i], ": ", i+1)
    i = i + 1

