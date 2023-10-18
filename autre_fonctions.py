def fic_to_text(fichier):
    texte_crypte = []
    res = []
    fic = open(fichier, 'r')
    les_lignes = fic.readlines()
    for ligne in les_lignes:
        res.append(ligne.replace("\n", ""))
        texte_crypte.append(ligne.replace("\n", ""))
    fic.close()
    return res

pangramme = "LE VIF ZEPHYR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX"

def premiere_apparition(texte):
    res = ""
    in_res = []
    for lettre in texte:
        if lettre != " " and lettre != ",":
            if lettre not in in_res:
                res += lettre
                in_res.append(lettre)
    return res

print(premiere_apparition(pangramme))