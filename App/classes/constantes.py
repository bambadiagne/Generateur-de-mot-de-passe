from hashlib import md5, sha256  # librairie permettant de hacher un mot de passe

HASH_DICT = {'md5': md5, 'sha256': sha256}
ALL_TYPES = {'numeric': list('0123456789'), 'alphalower': [chr(i) for i in range(97, 123)], 'alphaupper': [chr(i) for i in range(65, 91)], 'specialschars': [
    '[', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', ']'], 'alphanum': 1}

ALL_TYPES['alphanum'] = ALL_TYPES['alphalower'] + \
    ALL_TYPES['alphaupper']+ALL_TYPES['numeric']+ALL_TYPES['specialschars']
