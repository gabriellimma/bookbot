"""
Module for helper functions to the bookbot project on boot.dev
https://www.boot.dev/courses/build-bookbot-python
"""

def get_num_words(string_file):
    """
    Docstring for get_num_words
    
    :param str: string that will be word counted
    :return: number of total words found in a string
    :rtype: Integer
    """
    print("----------- Word Count ----------")
    split_result = string_file.split()
    return len(split_result)

def get_char_count(string_file):
    """
    Return the count of each character in a string.

    :param string_file: String to be evaluated.
    :type string_file: str

    :return: Dictionary containing the character counts, e.g. {'a': 1, 'b': 2}.
    :rtype: Dict[str, int]
    """
    result = {}
    file_words = string_file.split()
    for word in file_words:
        for char in word:
            result[char.lower()] = result.get(char.lower(), 0) + 1
    return result

def sort_on(items):
    """
    Helper function to sort
    
    :param items: Item to sort
    """
    return items["num"]

def sort_char_count(char_dict):
    """
    Function that transform a list of values into a dict
    {
        "char": a, # char name
        "num": 10  # occurrencies
    }
    
    :param char_dict: Description
    """
    print("--------- Character Count -------")
    result_dict = []
    for key, val in char_dict.items():
        result_dict.append({
            "char": key,
            "num": val
        })
    result_dict.sort(reverse=True, key=sort_on)
    return result_dict
        