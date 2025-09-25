import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_tekst(book):
    with open (book) as f:
        return f.read()
# Reads the book and return the text as a string
from stats import number_of_words
# Returns number of words in the text
from stats import character_count
# Returns a dictionary with keys as characters and values as counts of those characters in the text
from stats import sort_character_count
# Returns a sorted list of dictionaries with characters and their counts
def main(book):
    tekst = get_book_tekst(book)
    words = number_of_words(tekst)
    char_count = character_count(tekst)
    sorted_char_count = sort_character_count(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main(sys.argv[1])