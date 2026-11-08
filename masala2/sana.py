from datetime import datetime


def bugungi_sana():
    bugun = datetime.now()
    return bugun.strftime("%Y-%m-%d")


def hozirgi_vaqt():
    hozir = datetime.now()
    return hozir.strftime("%H:%M:%S")


def yilni_aniqla(sana):
    qismlar = sana.split("-")
    yil = int(qismlar[0])
    return yil
