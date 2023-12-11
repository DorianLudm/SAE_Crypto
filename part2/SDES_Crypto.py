from SDES import *

def cassage_brutal(message_clair, message_chiffre):
    """Cassage brutal de la clé"""
    set_res = set()
    for i in range(2**8):
        for j in range(2**8):
            if encrypt(i,message_clair) == decrypt(j,message_chiffre):
                set_res.add((i,j))
    return set_res
 
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

def test_brutal():
    import time
    import random
    start_time = time.time()
    passed = 0
    nb_test = 16
    for i in range(nb_test):
        msg = random.randint(0, 255)
        cle = random.randint(0, 255)
        msg_crypted = encrypt(cle, msg)
        cle2 = random.randint(0, 255)
        msg_crypted2 = encrypt(cle2, msg_crypted)
        keys = cassage_brutal(msg, msg_crypted2)
        if (cle, cle2) in keys:
            passed += 1
    time = time.time() - start_time
    print("Décodage Brutal 1! Taux de réussite:", passed/nb_test*100, "% sur", nb_test, "tests en", time, "secondes")
    
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

def encodage_texte(fichier):
    try:
        import random
        fic = open(fichier, 'r')
        text = []
        cle1 = random.randint(0, 255)
        cle2 = random.randint(0, 255)
        for ligne in fic.readlines():
            ligneCrypted = ""
            for char in ligne:
                ascii = ord(char)
                if 65 <= ascii <= 90 or 97 <= ascii <= 122:
                    crypted = encrypt(cle2, encrypt(cle1, ascii))
                    ligneCrypted = ligneCrypted + chr(crypted)
                else:
                    ligneCrypted = ligneCrypted + char
            text.append(ligneCrypted)
        fic.close()
        fic2 = open("./part2/Encoded_text", 'w')
        for ligne in text:
            fic2.write(ligne)
        fic2.close()
        print("Texte crypté!")
    except:
        print("Erreur lors de l'ouverture du fichier!")

encodage_texte("./part2/arsene_lupin_extrait.txt")
test_brutal()
test_astucieux()
test_astucieux2()