from stats import count_words
from stats import count_characters
from stats import sort_dict
from stats import print_book_stats
import sys

def get_book_text(filepath):
    with open(filepath) as file:
        contents = file.read()
    return contents

def main():
    try:
        filepath = sys.argv[1]
    except Exception as e:
        print(e)
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_contents = get_book_text(filepath)
    print(book_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_contents)} total words")
    
    char_dict = count_characters(book_contents)
    print(char_dict)
    print("--------- Character Count -------")
    sorted_dict = sort_dict(book_contents)
    print_book_stats(sorted_dict)
    return 0

main()