"""
Module for bookbot project on boot.dev
https://www.boot.dev/courses/build-bookbot-python
"""
import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(file_path):
    """
    Function that returns the contents of a file in a string.
    
    :param file_path: Path to the file
    :return: contents of a file
    :rtype: String
    """
    file_content = ""
    with open(file_path, encoding="utf-8") as f:
        print(f"Analyzing book found at {file_path}...")
        file_content = f.read()
    return file_content

def main():
    """
    Main method that calls and print the return of
    get_book_text
    """
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    stringfied_book = get_book_text(sys.argv[1])
    char_count = get_char_count(stringfied_book)

    print(f"Found {get_num_words(stringfied_book)} total words")
    sorted_char_array = sort_char_count(char_count)
    for char in sorted_char_array:
        print(f"{char['char']}: {char['num']}")

main()
