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
    dict_messageInTheMiddle = dict()
    for cle in range(1,2**8):
        #Passage de M à C1
        msg_crypted = encrypt(cle, message_clair)
        if msg_crypted in dict_messageInTheMiddle.keys():
            if encrypt(dict_messageInTheMiddle[msg_crypted], message_clair) == decrypt(dict_messageInTheMiddle[msg_crypted], message_chiffre):
                return (cle, dict_messageInTheMiddle[msg_crypted], msg_crypted)
        dict_messageInTheMiddle[msg_crypted] = cle

        #Passage de C2 à C1
        msg_decrypted = decrypt(cle, message_chiffre)
        if msg_decrypted in dict_messageInTheMiddle.keys():
            if encrypt(dict_messageInTheMiddle[msg_decrypted], message_clair) == decrypt(dict_messageInTheMiddle[msg_decrypted], message_chiffre):
                return (dict_messageInTheMiddle[msg_decrypted], cle, msg_decrypted)
        dict_messageInTheMiddle[msg_decrypted] = cle
        
    return None

# cassage_brutal(0b00010001,5,5)
# print("Les clés sont : ",cassage_brutal(0b00010001,5,5))    

msg = 0b00010001
cle = 0b00001101
msg_crypted1 = encrypt(cle, msg)
cle2 = 0b00001111
msg_crypted2 = encrypt(cle2, msg_crypted1)
print(cle, cle2)
print(msg, msg_crypted1, msg_crypted2)
# print(decrypt(cle2, msg_crypted2))
# print(msg_crypted1)
# print()
# print(decrypt(8, msg_crypted2))
# print(encrypt(12, msg))
print("Les clés sont : ",cassage_astucieux(msg, msg_crypted2))