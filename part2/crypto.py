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
    set_decoded = set_encoded = set()
    for cle in range(2**10):
        msg_crypted = encrypt(message_clair, cle)
        if msg_crypted in set_decoded:
            return cle
        set_encoded.add(message_chiffre)
        msg_decrypted = decrypt(message_chiffre, cle)
        if msg_decrypted in set_encoded:
            return cle
        set_decoded.add(msg_decrypted)
 
    
# cassage_brutal(0b00010001,5,5)
print("La clé est : ",cassage_brutal(0b00010001,5,5))    
print(cassage_astucieux(0b00010001, 0b01011101))