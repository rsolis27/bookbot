def main():
    book_path = "books/frankenstein.txt"
    text = get_book_path(book_path)
    num_words = word_count(text)
    num_chars = char_count(text)
    print(f"--- Begin of report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for char in num_chars:
        value = num_chars[char]
        if char.isalpha():
            print(f"The '{char}' character was found {value} times")
    print("--- End report ---")


def char_count(text):
    lower_case = text.lower()
    char_dict = {}
    for char in lower_case:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def word_count(text):
    words = text.split()
    return len(words)


def get_book_path(path):
    with open(path) as f:
        return f.read()


main()
