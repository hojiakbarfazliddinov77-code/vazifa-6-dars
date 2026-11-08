import random
import string


def parol_yarat(uzunlik):
    harflar = string.ascii_letters
    raqamlar = string.digits
    maxsus = "!@#$%^&*"
    belgilar = harflar + raqamlar + maxsus

    parol = ""
    for i in range(uzunlik):
        parol += random.choice(belgilar)
    return parol


def parol_tekshir(parol):
    if len(parol) >= 8:
        return True
    else:
        return False
