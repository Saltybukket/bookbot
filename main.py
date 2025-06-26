from stats import count_words
from stats import count_characters
from stats import sort_dict
from stats import print_book_stats

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    filepath = "../bookbot/books/frankenstein.txt"
    book_contents = get_book_text(filepath)
    #print(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_contents)} total words")
    
    #char_dict = count_characters(book_contents)
    #print(char_dict)
    print("--------- Character Count -------")
    sorted_dict = sort_dict(book_contents)
    print_book_stats(sorted_dict)
    return 0

main()