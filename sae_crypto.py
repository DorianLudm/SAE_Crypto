def dechiffrement_cesar(entree: str):
    for var_cle in range(26):
        res = dechiffrement_cesar_with_key(entree, var_cle)

def dechiffrement_cesar_with_key(entree: str, cle: int):
    string_res = ""
    for lettre in entree :
        lettre_decodee = ord(lettre) - cle
        if 65 <= ord(lettre) <= 90:    # Si la lettre est une minuscule
            if lettre_decodee < 65:
                lettre_decodee += 26
        elif 97 <= ord(lettre) <= 122: # Si la lettre est une majuscule
            if lettre_decodee < 97:
                lettre_decodee += 26
        string_res += lettre.lower()
    return string_res
    


message1 = "BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD " + "MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD " + "ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG " + "SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ " + "DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ " + "MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE. " + "YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD, " + "YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE, " + "QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD "
print(dechiffrement_cesar_with_key(message1, 12))

print(ord("A"), ord("Z"), ord("a"), ord("z"))

# res = 
# PRES DU CHEMIN SE CACHE UN TRESOR
# ACCROCHE A UN ARBRE TOUT RECOUVERT D'OR
# NE NEGLIGE PAS LA JEUNE POUCE FEUILLU
# GRAND EST SON SECRET MALGRE SA TAILLE MENUE
# RONDES ET COLOREES SONT LES BAIES QU'IL PORTE
# ANISEES ET SUCREES, LEURS SAVEURS SONT FORTES.
# MAIS ATTENTION A NE PAS LES CROQUER,
# MEME SI LA FAIM TIRAILLE TES ENTRAILLES,
# EN AUCUN CAS TU NE DOIS SUCCOMBER