def word_count(text):
    words = text.split()
    return len(words)


def char_count(text):
    lower_case = text.lower()
    char_dict = {}
    for char in lower_case:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def dict_to_list(dict):
    list_of_dicts = []
    for key, value in dict.items():
        list_of_dicts.append({"char": key, "count": value})
    return list_of_dicts


def sort_on(dict):
    return dict["count"]
