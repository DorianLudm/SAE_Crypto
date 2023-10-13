texte_crypte = []
ensemble_mot = set()

def main(fichier_mot, fichier_dico):
    fic_to_text(fichier_mot)
    # print(texte_crypte) #Affiche le texte crypté
    load_dictionnaire(fichier_dico)
    print(dechiffrement_cesar(texte_crypte))

def load_dictionnaire(fichier):
    global ensemble_mot
    fic = open(fichier, 'r')
    les_lignes = fic.readlines()
    for mot in les_lignes:
        ensemble_mot.add(mot.replace("\n", ""))
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
    return(mot in ensemble_mot)

def dechiffrement_cesar(entree: str):
    res = []
    for var_cle in range(26):
        entree_avec_cle = dechiffrement_cesar_with_key(entree, var_cle)
        if entree_avec_cle != False:
            res.append((var_cle, entree_avec_cle))
    return res

def dechiffrement_cesar_with_key(entree: list[str], cle: int):
    est_lisible = True
    cpt_mot = 0
    nb_mot_in_set = 0
    liste_res = []
    liste_char = [" ",",",";",".","_"]
    for ligne in entree:
        if not est_lisible:
            return False
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
                mot_courant += chr(lettre_decodee).lower()
                res_ligne += chr(lettre_decodee)
            elif mot_courant != "":
                res_ligne += lettre
                if lettre in liste_char:
                    cpt_mot += 1
                    nb_mot_in_set += mot_in_set(mot_courant)
                    mot_courant = ""
                    if cpt_mot >= 10:
                        est_lisible = nb_mot_in_set >= 8
                else:
                    mot_courant += lettre
        if mot_courant != "":
            cpt_mot += 1
            nb_mot_in_set += mot_in_set(mot_courant)
        liste_res.append(res_ligne)
    return liste_res

import time
start = time.time()

main("indice1_chiffre.txt", "dictionnaire_fr.txt")
end = time.time()
print(end - start)
