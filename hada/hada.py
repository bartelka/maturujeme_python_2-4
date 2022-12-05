fr = open("hada.txt", "r", encoding="utf-8")
max = 0
pocet_hier = 0
kopia_fr = open("hada_kopia.txt", "w", encoding="utf-8")
for riadok in fr:
    dlzka = len(riadok)
    pocet_hier += 1
    pocet = 0
    zoz = []
    for i in riadok:
       pocet += 1
       if pocet > max:
            max = pocet

print("Pocet hier:", pocet_hier, "\nPocet krokov najdlhsej hry: ", max)
