import string
import nltk
from nltk.corpus import stopwords


def main():
    nltk.download('stopwords')  # Only needed once
    stop_words = set(stopwords.words('english'))

    book_path = "books/frankenstein.txt" # Path of book

    text = get_book_text(book_path) # The actual book text itself

    num_words = get_num_words(text) # Number of words found in that book text

    letter_occurence = letter_dictionary(text) # creating local dictioanry of letter:amount

    list_of_dicts = [{"letter": letter, "count": count} for letter, count in letter_occurence.items()] # creating a list of dictionaries with their key:value names

    list_of_dicts.sort(reverse=True, key=sort_on) #sort by count, reversed.

    word_frequency = get_word_frequency(text)
    list_of_words_frequencies = [{"word": word, "count":count} for word, count in word_frequency.items()] # creating a list of dictionaries with their word:count attributes
    list_of_words_frequencies.sort(reverse=True, key=sort_on)

    # Begin printing formatting
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    # For each item in the list (which has the letter : letter and count : count pairs)
    for item in list_of_dicts:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    
    print("--- Begin section on word frequencies ---")
    counter = 0
    for item in list_of_words_frequencies:
        print(f"The '{item['word']}' word was found {item['count']}' times")
        counter += 1
        if (counter == 20):
            break
    print("--- End report ---")
    

# fucntion to get the number of words in the text
def get_num_words(text):
    words = text.split()
    return len(words)

# fucntion that returns a dictionary of letters and their occurence's by --> letter : occurence pairs
def letter_dictionary(text):
    letter_occurence = {letter: 0 for letter in string.ascii_lowercase}

    for word in text.split():
        for letter in word:
            if letter.isalpha():
                letter = letter.lower() 
                letter_occurence[letter] += 1
    return letter_occurence

# function that opens the book file and returns the read text
def get_book_text(path):
    with open(path) as f:
        return f.read()

# function that sorts the dictionary by the 'count's 
def sort_on(dict):
    return dict['count']

def get_word_frequency(text):
    stop_words = set(stopwords.words('english'))
    word_dict = {}
    for word in text.split():
        word = word.lower()
        if (word.isalpha() and word in word_dict):
            word_dict[word] += 1
        elif (word not in stop_words and word.isalpha()):
            word_dict[word] = 1
    return word_dict



main()
