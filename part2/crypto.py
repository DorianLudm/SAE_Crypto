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
    for cle in range(2**8):
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

def cassage_astucieux2(message_clair, message_chiffre):
    """Cassage astucieux de la clé"""
    dict_encoded = dict()
    dict_decoded = dict()
    test_cle = set()
    for cle in range(2**8):
        #Passage de M à C1
        msg_crypted = encrypt(cle, message_clair)
        if msg_crypted in dict_decoded.keys():
            for cle_decrypt in dict_decoded[msg_crypted]:
               if decrypt(cle_decrypt, message_chiffre) == msg_crypted:
                   test_cle.add((cle, cle_decrypt, msg_crypted ))

        if not msg_crypted in dict_encoded:
            dict_encoded[msg_crypted] = []
        dict_encoded[msg_crypted].append(cle)

        #Passage de C2 à C1
        msg_decrypted = decrypt(cle, message_chiffre)
        if msg_decrypted in dict_encoded.keys():
            for cle_crypt in dict_encoded[msg_decrypted]:
               if encrypt(cle_crypt, message_clair) ==  msg_decrypted:
                   test_cle.add((cle_crypt, cle, msg_decrypted))
        if not msg_decrypted in dict_decoded:
            dict_decoded[msg_decrypted] = []
        dict_decoded[msg_decrypted].append(cle)

    return test_cle

def test_astucieux():
    import time
    import random
    start_time = time.time()
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
    time = time.time() - start_time
    print("Décodage astucieux 1! Taux de réussite:", passed/nb_test*100, "% sur", nb_test, "tests en", time, "secondes")

def test_astucieux2():
    import time
    import random
    start_time = time.time()
    passed = 0
    nb_test = 2048
    for i in range(nb_test):
        msg = random.randint(0, 255)
        cle = random.randint(0, 255)
        msg_crypted = encrypt(cle, msg)
        cle2 = random.randint(0, 255)
        msg_crypted2 = encrypt(cle2, msg_crypted)
        keys = cassage_astucieux2(msg, msg_crypted2)
        if (cle, cle2, msg_crypted) in keys:
            passed += 1
    time = time.time() - start_time
    print("Décodage astucieux 2! Taux de réussite:", passed/nb_test*100, "% sur", nb_test, "tests en", time, "secondes")

test_astucieux()
test_astucieux2()