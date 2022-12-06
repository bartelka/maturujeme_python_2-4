fr = open("hada.txt", "r", encoding="utf-8")
max = 0
pocet_hier = 0
kopia_fr = open("hada_kopia.txt", "w", encoding="utf-8")
for riadok in fr:
    dlzka = len(riadok)-1
    pocet_hier += 1
    if dlzka > max:
        max = dlzka
fr = open("hada.txt", "r", encoding="utf-8")
for riadok in fr:
    poc = 0
    zoz = list(riadok)
    pismenko = zoz[0]
    hotovecka = ""
    taky_zoz = []
    for i in range(len(riadok)):
        poc += 1
        if pismenko != zoz[0]:
            if poc > len(taky_zoz):
                poc -= 1
            hotovecka = hotovecka + pismenko + str(poc)
            pismenko = zoz[0]
            poc = 0
            taky_zoz = []
        taky_zoz += [pismenko]
        del zoz[0]
    hotovecka += "\n"
    kopia_fr.write(hotovecka)

print("Pocet hier:", pocet_hier, "\nPocet krokov najdlhsej hry: ", max)
