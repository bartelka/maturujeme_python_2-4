fr = open("objednane_jedla.txt", "r", encoding="utf-8")

pocet_jedal = 0
objednane_jedla = {"z":0, "c":0, "m":0, "o":0}
menej_ako_20 = " "

for riadok in fr:
    pocet_jedal += 1
    for i in riadok:
        if i in objednane_jedla:
            objednane_jedla[i] +=1

print("počet jedál:",str(pocet_jedal))

for jedlo, pocet in objednane_jedla.items():
    print("Jedlo - číslo kódu:", jedlo, "počet objednaní:", str(pocet))
    if pocet < 20:
        menej_ako_20 += jedlo + " "

if menej_ako_20 != " ":
    print("Jedlá:", menej_ako_20, "boli objednané menej ako 20-krát.")
else:
    print("Každé jedlo si objednalo dostatok stravníkov.")