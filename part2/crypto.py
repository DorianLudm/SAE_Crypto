from SDES import *

def cassage_brutal(message_chiffre, taille_cle1,taille_cle2):
    """Cassage brutal de la clé"""
    for i in range(2**taille_cle1):
        for j in range(2**taille_cle2):
            if decrypt(i,decrypt(j,message_chiffre)) == 0b00000000:
                return (i,j)
    return (0,0)
 
def cassage_astucieux(message_clair, message_chiffre):
    """Cassage astucieux de la clé"""
    dict_encoded = dict()
    dict_decoded = dict()
    set_res = set()
    for cle in range(1,2**8):
        #Passage de M à C1
        msg_crypted = encrypt(cle, message_clair)
        if msg_crypted in dict_decoded.keys():
            set_res.add((cle, dict_decoded[msg_crypted]))
        dict_encoded[msg_crypted] = cle

        #Passage de C2 à C1
        msg_decrypted = decrypt(cle, message_chiffre)
        if msg_decrypted in dict_encoded.keys():
            set_res.add((dict_encoded[msg_decrypted], cle))
        dict_decoded[msg_decrypted] = cle
        
    return set_res

import random
passed = 0
nb_test = 2048
for i in range(nb_test):
    msg = random.randint(0, 255)
    cle = random.randint(0, 255)
    msg_crypted = encrypt(cle, msg)
    cle2 = random.randint(0, 255)
    msg_crypted2 = encrypt(cle2, msg_crypted)
    keys = cassage_astucieux(msg, msg_crypted2)
    if (cle, cle2) in keys:
        passed += 1
print("Taux de réussite:", passed/nb_test*100, "%")