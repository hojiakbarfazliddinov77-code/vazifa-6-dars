import requests

URL = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"

kod = input("Valyuta kodini kiriting: ").strip().upper()

try:
    miqdor = float(input("Miqdorni kiriting: "))
except ValueError:
    print("Miqdor noto'g'ri kiritildi! Faqat son kiriting.")
    exit()

if miqdor <= 0:
    print("Miqdor 0 dan katta bo'lishi kerak!")
    exit()

try:
    javob = requests.get(URL, timeout=10)
    javob.raise_for_status()
    kurslar = javob.json()
except requests.exceptions.RequestException:
    print("API ga ulanib bo'lmadi. Internetni tekshiring.")
    exit()

topildi = None
for valyuta in kurslar:
    if valyuta["Ccy"] == kod:
        topildi = valyuta
        break

if topildi is None:
    print("Bunday valyuta kodi topilmadi!")
else:
    nom = topildi["CcyNm_UZ"]
    nominal = float(topildi["Nominal"])
    kurs = float(topildi["Rate"]) / nominal
    jami = miqdor * kurs

    print()
    print("Valyuta:", nom)
    print("Miqdor:", miqdor, kod)
    print(f"1 {kod} kursi: {kurs:.2f} so'm")
    print()
    print(f"Jami: {jami:.2f} so'm")