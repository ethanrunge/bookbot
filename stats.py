def find_num_words(string):
    """
    given a string, this function will find the number of words it contains
    """
    split_string_by_word = string.split()
    return len(split_string_by_word)

def number_of_each_character(string):
    """
    given a string, this function will determine how many of each character
    appears in the string
    """
    characters_in_book = {}
    string_lower = string.lower()
    for char in string_lower:
        if char not in characters_in_book:
            characters_in_book[char] = 1
        elif char in characters_in_book:
            characters_in_book[char] += 1
        else:
            continue
    return characters_in_book

def sort_dictionary_of_chars(dict_of_chars):
    """
    This function takes a dictionary that counts how many of each character appears
    in a body of text and orders it from most to least occurences
    """
    sorted_list = []
    for item in dict_of_chars:
        if item.isalpha():
            sorted_list.append({"char": item, "num": dict_of_chars[item]})
        else:
            continue
    sorted_list.sort(key=sort_by_item, reverse=True)
    return sorted_list

def sort_by_item(items):
    return items["num"]
