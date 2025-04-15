from stats import char_count, word_count, dict_to_list, sort_on
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_path(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    list_of_chars = dict_to_list(num_chars)
    list_of_chars.sort(reverse=True, key=sort_on)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list_of_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


def get_book_path(path):
    with open(path) as f:
        return f.read()


main()
