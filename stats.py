def word_count(book_text):
    num_words = 0
    words = book_text.split()
    for word in words:
        num_words += 1
    return num_words

def char_count(book_text):
    char_dict = {}
    for t in book_text:
        char = t.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sorted_list(char_dict):
    dict_list = []
    for char in char_dict:
        new_dict = {"char": char, "num": char_dict[char]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=lambda d: d["num"])
    return dict_list
