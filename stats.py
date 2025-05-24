def get_num_words(book_contents):
    count = 0
    for words in book_contents.split():
        count += 1
    return count


def get_num_chars(book_contents):
    char_num = {}
    for words in book_contents.split():
        for char in words.lower():
            if char not in char_num:
                char_num[char] = 1
            else:
                char_num[char] += 1
    return char_num


def sort_dict(char_num):
    return dict(sorted(char_num.items(), reverse=True, key=lambda item: item[1]))
