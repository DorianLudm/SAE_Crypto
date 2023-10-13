liste = ["PRES DU CHEMIN SE CACHE UN TRESOR", "ACCROCHE A UN ARBRE TOUT RECOUVERT DOR", "NE NEGLIGE PAS LA JEUNE POUCE FEUILLU", "GRAND EST SON SECRET MALGRE SA TAILLE MENUE", "RONDES ET COLOREES SONT LES BAIES QUIL PORTE","ANISEES ET SUCREES LEURS SAVEURS SONT FORTES", "MAIS ATTENTION A NE PAS LES CROQUER", "MEME SI LA FAIM TIRAILLE TES ENTRAILLES", "EN AUCUN CAS TU NE DOIS SUCCOMBER"]

def nombre_premiere_lettre(msg):
    i = 0
    dic = dict()
    for ligne in msg:
        liste_mot = ligne.split(" ")
        for mot in liste_mot:
            for lettre in mot:
                if lettre not in dic.keys():
                    i += 1
                    dic[lettre] = i
                
    return dic

# print(nombre_premiere_lettre(liste))

mc = "ETLWKWKODLWFXPLPSFBFVKIFLZKOTSRTFDCFBRXFEFCH"
m = "BRAVOVOUSAVEZGAGNELECODEAFOURNIRESTELIZEBETH"

def calc_decalage(message_crypte, message):
    dic_trans = dict()
    if len(message) != len(message_crypte):
        return "ERREUR LONGUEUR DES MOTS"
    for index in range(len(message)):
        lettre_crypte = message_crypte[index]
        lettre = message[index]
        int_trans = ord(lettre_crypte) - ord(lettre)
        while int_trans >= 26:
            int_trans -= 26
        while int_trans < 0:
            int_trans += 26
        if lettre_crypte not in dic_trans.keys():
            dic_trans[lettre_crypte] = (int_trans, lettre)
        else:
            print(dic_trans[lettre_crypte] == (int_trans, lettre))
    return dic_trans

print(calc_decalage(mc, m))