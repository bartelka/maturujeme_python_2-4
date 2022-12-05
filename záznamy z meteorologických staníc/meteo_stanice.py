fr = open("meteo_stanice.txt", "r", encoding="utf-8")
pocet_merani = 0
sucet = 0
max = 0
for riadok in fr:
    pocet_merani += 1
    riadok.strip()
    riadok = riadok.replace(",", ".")
    dlzka = len(riadok)
    cislo = ""
    for i in range(dlzka):
        if riadok[i] in "+-":
            for x in range(5):
                x = i+x
                cislo += riadok[x]
            print("namerana teplota:", cislo)
            sucet += float(cislo)
    cislo = float(cislo)
    if max < cislo:
        max = cislo
fr = open("meteo_stanice.txt", "r", encoding="utf-8")
max = str(max)
kod = ""
for riadok in fr:
    riadok.strip()
    riadok = riadok.replace(",", ".")
    if max in riadok:
        for i in range(3):
            kod += riadok[i]
priemer = sucet / pocet_merani
print("Pocet merani:", pocet_merani, "\nNajvacsia namerana teplota:", max,"\nKod tanice najvyssej teploty:",kod, "\nPriemerna teplota:", round(priemer,2))
