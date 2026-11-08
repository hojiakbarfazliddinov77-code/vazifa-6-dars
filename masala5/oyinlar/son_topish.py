import random


def son_yarat(minimum, maksimum):
    return random.randint(minimum, maksimum)


def tekshir(taxmin, sirli_son):
    if taxmin < sirli_son:
        return "Kichik"
    elif taxmin > sirli_son:
        return "Katta"
    else:
        return "To'g'ri"