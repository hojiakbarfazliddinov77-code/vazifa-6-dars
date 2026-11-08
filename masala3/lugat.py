def soz_qosh(lugat, soz, tarjima):
    lugat[soz] = tarjima


def soz_qidir(lugat, soz):
    return lugat.get(soz, "Bunday so'z lug'atda yo'q")


def lugatni_kor(lugat):
    if not lugat:
        print("Lug'at bo'sh")
        return
    for soz, tarjima in lugat.items():
        print(f"{soz} - {tarjima}")