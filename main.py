# main.py
"""
author = klaus.kapllani@esiee.fr
"""

from unicodedata import normalize

def ispalindrome(p):
    """
    Détermine si p est un palindrome.

    Args : 
        p : string

    Returns :
        ispalindrome(p) : True si c'est un palindrome, sinon False
    """

    i = 0
    j = len(p) - 1
    while i<j:
        # Ignore les caractères non alphanumériques et les espaces
        while i < j and not p[i].isalnum():
            i += 1
        while i < j and not p[j].isalnum():
            j -= 1

        # Supprime les accents et met les caractères en minuscule,
        # puis compare les lettres
        if normalize('NFD', p[i]).encode(
            'ascii', 'ignore').decode().lower() != normalize(
            'NFD', p[j]).encode('ascii', 'ignore').decode().lower():
            return False
        i += 1
        j -= 1
    return True

def main():
    """
    Fonction principale qui affiche si les exemples suivants sont des palindromes ou non.

    Returns :
        rien
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, "est un palindrome." if ispalindrome(s) else "n'est pas un palindrome.")

if __name__ == "__main__":
    main()
