# Antra užduotis
#
# Sukurti funkciją, kuri priimtų tuple ir grąžintų kitą tuple, tik su pašalintais dublikatais. Eiliškumas elementų turi išlikti toks pats:
# Pvz: jeigu funkcija priima (1, 2, 3, 4, 3, 2, 1) tuple, tai turėtų grąžinti (1, 2, 3, 4)
# Pvz: jeigu funkcija priima (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’, ‘q’, ‘h’, ‘d’) tuple, tai turėtų grąžinti (‘a’, ‘d’, ‘g’, ‘h’, ‘i’, ‘q’)
# Paduoti tuple į funkciją (reikšmes sugalvokite patys) ir išspausdinti funkcijos rezultatą


skaiciai = (1, 2, 3, 4, 3, 2, 1)

def remove_dublicates(skaiciai):
    new_skaiciai = []
    for skaicius in skaiciai:
        if skaicius not in new_skaiciai:
            new_skaiciai.append(skaicius)
    return new_skaiciai
new_skaiciai = remove_dublicates(skaiciai)
print(new_skaiciai)
