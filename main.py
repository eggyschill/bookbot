import string

def main():
    book_path = "books/frankenstein.txt" # Path of book

    text = get_book_text(book_path) # The actual book text itself

    num_words = get_num_words(text) # Number of words found in that book text

    letter_occurence = letter_dictionary(text) # creating local dictioanry of letter:amount

    list_of_dicts = [{"letter": letter, "count": count} for letter, count in letter_occurence.items()] # creating a list of dictionaries with their key:value names

    list_of_dicts.sort(reverse=True, key=sort_on) #sort by count, reversed.

    # Begin printing formatting
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    # For each item in the list (which has the letter : letter and count : count pairs)
    for item in list_of_dicts:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    
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

main()
