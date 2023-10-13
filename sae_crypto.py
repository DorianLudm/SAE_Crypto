texte_crypte = []
ensemble_mot = set()

def main(fichier_mot, fichier_dico):
    fic_to_text(fichier_mot)
    load_dictionnaire(fichier_dico)
    print(dechiffrement_cesar_with_key(texte_crypte, 12))

def load_dictionnaire(fichier):
    global ensemble_mot
    fic = open(fichier, 'r')
    les_lignes = fic.readlines()
    for mot in les_lignes:
        ensemble_mot.add(mot)
    fic.close()

def fic_to_text(fichier):
    global texte_crypte
    res = []
    fic = open(fichier, 'r')
    les_lignes = fic.readlines()
    for ligne in les_lignes:
        res.append(ligne.replace("\n", ""))
        texte_crypte.append(ligne.replace("\n", ""))
    fic.close()
    return res

def mot_in_set(mot: str):
    global ensemble_mot
    return mot in ensemble_mot

def dechiffrement_cesar(entree: str):
    for var_cle in range(26):
        res = dechiffrement_cesar_with_key(entree, var_cle)

def dechiffrement_cesar_with_key(entree: list[str], cle: int):
    liste_res = []
    liste_char = [" ",",",";",".","_"]
    for ligne in entree:
        mot_courant = ""
        res_ligne = ""
        for lettre in ligne:
            lettre_decodee = ord(lettre) - cle
            if 65 <= ord(lettre) <= 90:    # Si la lettre est une minuscule
                if lettre_decodee < 65:
                    lettre_decodee += 26
            elif 97 <= ord(lettre) <= 122: # Si la lettre est une majuscule
                if lettre_decodee < 97:
                    lettre_decodee += 26
            if 65 <= lettre_decodee <= 90 or 97 <= lettre_decodee <= 122:
                mot_courant += chr(lettre_decodee)
                res_ligne += chr(lettre_decodee)
            elif mot_courant != "":
                res_ligne += lettre
                if lettre in liste_char:
                    print(mot_courant)
                    mot_courant = ""
                else:
                    mot_courant += lettre
        if mot_courant != "":
            print(mot_courant)
        liste_res.append(res_ligne)
    return liste_res

main("indice1_chiffre.txt", "dictionnaire_fr.txt")