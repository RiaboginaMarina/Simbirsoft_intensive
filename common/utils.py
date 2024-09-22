import string
import random


def generate_random_number(length):
    rand_number = ''
    for i in range(length):
        rand_number += str(random.randint(0, 9))
    return rand_number


def create_word_from_number(number):
    alphabet = string.ascii_lowercase
    word = ''
    while number:
        letter_number = int(number[:2])
        word += alphabet[letter_number % 26]
        number = number[2:]
    return word


def generate_random_word(length):
    alphabet = string.ascii_lowercase
    return ''.join(random.choice(alphabet) for _ in range(length))


def convert_table_data_to_list(table_data):
    result = []
    for line in table_data.split('\n')[1:]:
        result.append(line.split())
    return result
