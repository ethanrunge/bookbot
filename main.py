from stats import find_num_words, number_of_each_character, sort_dictionary_of_chars
import sys

def get_book_text(path_to_book):
    """
    Finds the book given in the path and returns the text as a string
    """
    with open(path_to_book) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) == 2:
        path = sys.argv[1]
        book_text = get_book_text(path)
        word_count = find_num_words(book_text)
        num_each = number_of_each_character(book_text)
        sorted_characters = sort_dictionary_of_chars(num_each)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for character in sorted_characters:
            print(f"{character["char"]}: {character["num"]}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()