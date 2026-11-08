import baholash

oquvchilar = {
    "Ali": 95,
    "Vali": 82,
    "Sardor": 67,
    "Malika": 45,
    "Dilnoza": 78
}

for ism, ball in oquvchilar.items():
    print(f"{ism}: {ball} ball - {baholash.baho_aniqla(ball)}")

balllar = list(oquvchilar.values())

print("O'rtacha ball:", baholash.ortacha_hisobla(balllar))
print("Eng yuqori ball:", baholash.eng_yaxshi_ball(balllar))