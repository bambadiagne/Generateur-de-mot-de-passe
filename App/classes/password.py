from random import sample, choice, shuffle
from .constantes import ALL_TYPES


class Password:
    def __init__(self, password_type, password_length=8):

        self.password_length = password_length
        self.password_type = password_type

    def gen_password(self, tabMotif):
        generated_password = self.randomPassword(tabMotif)
        while not all(any(letter in ALL_TYPES[motif] for letter in generated_password) for motif in tabMotif):
            generated_password = self.randomPassword(tabMotif)
        return generated_password

    def randomPassword(self, tabMotif):
        passTab = list(choice([elt for type_password in tabMotif for elt in ALL_TYPES[type_password]])
                       for i in range(int(self.password_length)))
        shuffle(passTab)
        return ''.join(passTab)
