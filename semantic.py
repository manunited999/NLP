# import the module
import spacy

# load the language model
nlp = spacy.load('en_core_web_md')

# define words as nlp applied to the required words
word1 = nlp("cat")
word2 = nlp('monkey')
word3 = nlp('banana')

# use similarity to find and print the similarity between two words
# the answer will be given by a number
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# What's interesting is that there is the highest similarity between animals, cat and monkey but it is not very high
# There is a bigger similarity between monkey and banana, and cat and banana which makes sense because monkeys are associated with eating bananas

print("\n")

# Here, I am testing my own words to see the similarity, in a similar way to above
word5 = nlp("steak")
word6 = nlp("cow")
word7 = nlp("human")

print(word5.similarity(word6))
print(word6.similarity(word7))
print(word7.similarity(word5))

print("\n")

# this is a setence where each word is a token
tokens = nlp('cat apple monkey banana ')

# it takes two sets of tokens such that two words can be compared, this allows all words to be compared
for token1 in tokens:
    for token2 in tokens:
# print out the name of both tokens and the similarity, for all possible combinations
        print(token1.text, token2.text, token1.similarity(token2))

# sentence to compare
sentence_to_compare = "Why is my cat on the car"

# list of sentences
sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana"
]

print("\n")

# apply the language module to the sentence to compare
model_sentence = nlp(sentence_to_compare)

# for each of the sentences in the list
for sentence in sentences:
    # find the similarity betwen the sentence and the one comparison sentence
    similarity = nlp(sentence).similarity(model_sentence)
    # print out the sentence, dash and then its similarity.
    print(sentence + " - ", similarity)


"""

When using en_core_web_sm, as a smaller module, there are no word vectors. This means that there will be less accurate similarity scores when using the similarity function. Using a larger module such as the md one will come with pre-trained word vectors. 

"""