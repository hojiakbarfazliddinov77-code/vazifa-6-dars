from parol import parol_yarat, parol_tekshir

uzunlik = int(input("Parol uzunligini kiriting: "))

yangi_parol = parol_yarat(uzunlik)
print("Yaratilgan parol:", yangi_parol)

print("Tekshiruv (abc):", parol_tekshir("abc"))
print("Yangi parol tekshiruvi:", parol_tekshir(yangi_parol))
