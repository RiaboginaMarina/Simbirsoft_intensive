import random
import string


def generate_random_number(length):
    rand_number = ''
    for i in range(length):
        rand_number += str(random.randint(0, 9))
    return rand_number


def create_word_from_number(number):
    word = ''
    while number:
        letter_number = int(number[:2])
        word += string.ascii_lowercase[letter_number % 26]
        number = number[2:]
    return word


def generate_random_word(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def convert_table_data_to_list(table_data):
    return [line.split() for line in table_data.split('\n')[:1]]
