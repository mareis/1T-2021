import random

liste_ord = ['Bredbånd', 'Bredformat', 'Byte', 'Bit', 'Grensesnitt', 'Internett', 'Komprimering', 'Kryptering', 'Innrykk']
def trekk_ord():
    tilfeldig = random.randint(0, len(liste_ord) - 1)
    return liste_ord[tilfeldig]
    