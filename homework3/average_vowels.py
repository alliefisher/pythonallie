# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()
    

# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

string = list(paragraph)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

# -- 1. Counting Vowels --
def counting_vowels_and_consonants(string):
    num_vowels = 0
    num_consonants = 0
    vowels = ["a", "e", "i", "o", "u"]
    for i in string:
        if i.isalpha():
            if i in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
    return (num_vowels, num_consonants)

num_vowels, num_consonants = counting_vowels_and_consonants(string)
print(f"The number of vowels in my string {num_vowels}, and the number of of consonants is {num_consonants}")

# -- 2. Average Vowels --
def average_values_and_consonants(paragraph):
    splits = paragraph.split(". ") # Came to office hours and talked to Pranathi and she said this was good!
    v = 0
    c = 0
    num_sentences = len(splits)
    for sentence in splits:
        num_vowels, num_consonants = counting_vowels_and_consonants(sentence) 
        v += num_vowels
        c += num_consonants
    average_v = v/num_sentences
    average_c = c/num_sentences
    return(num_sentences, average_v, average_c)

num_sentences, average_v, average_c = average_values_and_consonants(paragraph)
print(f"The number of sentences in my string is {num_sentences}, the average number of vowels is {average_v}, and the average number of consonants is {average_c}.")
    