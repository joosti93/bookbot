def get_book_tekst(book):
    with open (book) as f:
        return f.read()
from stats import number_of_words
from stats import character_count
def main():
    book = "books/frankenstein.txt"
    tekst = get_book_tekst(book)
    words = number_of_words(tekst)
    char_count = character_count(tekst)
    print(f"Found {words} total words")
    print(char_count)
main()