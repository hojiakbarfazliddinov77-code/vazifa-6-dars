import lugat

sozlar = {}

lugat.soz_qosh(sozlar, "apple", "olma")
lugat.soz_qosh(sozlar, "book", "kitob")
lugat.soz_qosh(sozlar, "water", "suv")
lugat.soz_qosh(sozlar, "house", "uy")
lugat.soz_qosh(sozlar, "friend", "do'st")

print("apple:", lugat.soz_qidir(sozlar, "apple"))
print("cat:", lugat.soz_qidir(sozlar, "cat"))

print("\nBarcha so'zlar:")
lugat.lugatni_kor(sozlar)