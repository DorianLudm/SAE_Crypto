def decalage(lettre:str):
    ascii = ord(lettre)
    if 65 <= ascii <= 90:
        return ascii - 65
    elif 97 <= ascii <= 122:
        return ascii - 97
    return None

def calc_len_msg(msg: list[str]):
    res = 0
    for ligne in msg:
        for lettre in ligne:
            res += (65 <= ord(lettre) <= 90 or 97 <= ord(lettre) <= 122)
    return res

def decode_vigenere(msg: list[str], cle: str):
    res = []
    while calc_len_msg(msg) > len(cle):
        cle = cle*2
    indice_cle = 0
    for ligne in msg:
        res_ligne = ""
        for lettre in ligne:
            lettre_decodee = ord(lettre) - decalage(cle[indice_cle])
            if 65 <= ord(lettre) <= 90:    # Si la lettre est une minuscule
                if lettre_decodee < 65:
                    lettre_decodee += 26
            elif 97 <= ord(lettre) <= 122: # Si la lettre est une majuscule
                if lettre_decodee < 97:
                    lettre_decodee += 26
            if 65 <= ord(lettre) <= 90 or 97 <= ord(lettre) <= 122:
                res_ligne += chr(lettre_decodee)
                indice_cle += 1
            else:
                res_ligne += lettre
        res.append(res_ligne)
    return res
    
message_code = ["AE IOW ZQBLNR WASIXQ WJR YKJ KGYUJAGY UU OXSLN TXRCUQYM",
"IY IRCTQ HPNF RR RQBIIIGOFN XQ WTCEKK DQ OIH MHXDUDQW BAYNVUDQYM",
"NR MRRPQD SU CXVMUQV HOHLWLQ CYT LRY GRQYMTRRY RPBMVXTVUES",
"QF EXNFO UEHAMAEM RV MQEWPGR IRCTQ HTREOVRQ XE HUOYKIFGXXOA"]

import time
start = time.time()

cle = "PANGRAMME"
msg_decode = decode_vigenere(message_code, cle)
print(msg_decode)

end = time.time()
print(end - start)