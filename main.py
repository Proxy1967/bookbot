from stats import get_num_words, get_num_chars, sort_dict
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    num_dict = get_num_chars(file_contents)
    sorted_dict = sort_dict(num_dict)
    print_report(book_path, num_words, sorted_dict)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report(book_path, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for key, value in sorted_dict.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")


main()
