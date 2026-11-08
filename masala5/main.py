from oyinlar import son_topish, tanga

print("Son topish o'yini (1 dan 100 gacha)")
sirli_son = son_topish.son_yarat(1, 100)

while True:
    taxmin = int(input("Taxminingiz: "))
    natija = son_topish.tekshir(taxmin, sirli_son)
    print(natija)
    if natija == "To'g'ri":
        print("Tabriklaymiz, topdingiz!")
        break

print("\nTanga tashlash:")
print("Natija:", tanga.tanga_tashla())