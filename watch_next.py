# import the module
import spacy

# use the en_core_web_md language module from spacy
nlp = spacy.load('en_core_web_md')

# define the function, which takes in the argument of a movie description
def find_most_similar_movie(description):
# open the movies file, and read its content into a variable
    with open("movies.txt", "r") as file:
        contents = file.read()
        # convert the contents into a list
        movie_list = contents.split("\n")

# the comparison is the language model applied to the movie description that we're passing into the function
    comparison = nlp(description)
    # this is a starting point to use so that we can find the maximum similarity
    max_similarity = -1
    # this is a placeholder which holds the highest similarity which will be replaced if there is a movie whith a higher similarity
    most_similar_movie = ""

# for each movie in the movie list
    for movie in movie_list:
# find the similarity between the movie and comparison
        similarity = nlp(movie).similarity(comparison)
# if that similarity is higher than the max_similarity variable
        if similarity > max_similarity:
# swap the variable with the similarity number of that movie
            max_similarity = similarity
# swap the name of the movie that is in the most_similar_movie with the movie with the higher similarity
            most_similar_movie = movie
# return the most similar movie
    return most_similar_movie

# define the planet hulk description from the task
planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
# the most similar movie is equal to the function, with the planet hulk description passed through
most_similar_movie = find_most_similar_movie(planet_hulk_description)

# print out the most similar movie
print("Most similar movie to 'Planet Hulk': \n\n", most_similar_movie)

