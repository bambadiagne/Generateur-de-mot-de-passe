
from .constantes import HASH_DICT, ALL_TYPES
from threading import Thread
from timeit import default_timer as timer
from queue import Queue


def hash_word(word, hash_function):
    return HASH_DICT[hash_function](str(word).encode()).hexdigest()


def import_file(filename):
    file_content = []
    with open(filename, "r") as file:
        file_content = file.read().split("\n")
    return file_content


def break_with_dict(hashes_filename, dict_filename, hash_function):
    hashes = import_file(hashes_filename)
    dict_words = import_file(dict_filename)
    return [(word, hash_word(word, hash_function)) for word in dict_words if(hash_word(word, hash_function) in hashes)]


def brute_force(pwd, pos, siz=8, chars="", hashes="", hash_function="", found_words=[]):

    if (pos < siz):
        for ch in chars:

            print(ch)
            brute_force(pwd + ch, pos + 1, siz, chars, hashes, hash_function)

    else:
        print('word ', pwd)
        pass

    return found_words


def brute_force_len(chars, hashes, len_word, hash_function):
    found_words = []
    for i in range(1, len_word+1):
        found_words.extend(brute_force("", 0, i, chars, hashes, hash_function))
    return found_words


class Crack(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            n = self.queue.get()
            result = 2
            self.queue.task_done()
