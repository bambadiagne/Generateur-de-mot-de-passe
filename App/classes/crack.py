from hashlib import md5, sha256  # librairie permettant de hacher un mot de passe


def break_with_dict(hashes_filename, dict_filename):
    # On ouvre le fichier contenant les mots de passe hachés
    with open(hashes_filename, "r") as hashes:
        # On recupere les haches dans une listes
        ALL_HASHES = hashes.read().split("\n")
        # On ouvre le fichier contenant le dictionnaire de mots
        with open(dict_filename, "r") as dict_words:

            # On hache chaque mot du dictionnaire et on verifie s'il est dans les hachés
            # On enregistre dans le mot  trouvé dans une liste
            # On renvoie la liste
            return [word for word in dict_words.read().split("\n") if(md5(str(word).encode()).hexdigest() in ALL_HASHES)]
#found_words=[hashlib.md5(str(word).encode()).hexdigest()  for word in break_with_dict("hashes.txt","dict.txt")]


def brute_force(pwd, pos, siz, chars, hashes, found_words=[]):

    if (pos < siz):
        for ch in chars:
            brute_force(pwd + ch, pos + 1, siz, chars)
    else:
        if(md5(str(pwd).encode()).hexdigest() in hashes):
            found_words.append(pwd, md5(str(pwd).encode()).hexdigest())
    return found_words


def brute_force_len(chars, len_word):
    found_words = []
    for i in range(1, len_word+1):
        found_words.extend(brute_force("", 0, i, chars, ""))
