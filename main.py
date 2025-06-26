from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    book_contents = get_book_text("../bookbot/books/frankenstein.txt")
    #print(book_contents)
    print(f"\n{count_words(book_contents)} words found in the document")
    char_dict = count_characters(book_contents)
    print(char_dict)
    return 0

main()