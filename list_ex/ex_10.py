# # https://www.w3resource.com/python-exercises/list/
# # Write a Python program to find the list of words that are longer than n from a given list of words.

list_of_words = ["ble", "ds", "fasg", "c", "dagsge", "scd"]


def word_length(word):
    if len(word) > 3:
        return word
    else:
        return None


def check_length(words_list):
    new_list_of_words = []
    for word in words_list:
        long_word = word_length(word)
        if long_word:
            new_list_of_words.append(long_word)

    return new_list_of_words


print("List of words linger than 3 letters: ", check_length(list_of_words))
