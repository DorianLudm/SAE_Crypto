def get_dic_transformation(clé):
    res = dict()
    indice_cle = 0
    alphabet_min = "abcdefghijklmnopqrstuvwxyz"
    alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for lettre in clé:
        if 65 <= ord(lettre) <= 90:
            if lettre not in res.keys():
                res[lettre] = alphabet_min[indice_cle]
                res[lettre.upper()] = alphabet_maj[indice_cle]
                indice_cle += 1
        elif 97 <= ord(lettre) <= 122:
            if lettre not in res.keys():
                res[lettre] = alphabet_maj[indice_cle]
                res[lettre.lower()] = alphabet_min[indice_cle]
                indice_cle += 1
    return res

def substitution(message_c, cle):
    dico_transf = get_dic_transformation(cle)
    res = ""
    for lettre in message_c:
        if lettre in dico_transf.keys():
            res += dico_transf[lettre]
        else:
            res += lettre
    return res

import time
start = time.time()

print(substitution("EALOK, OKCT LOFX PLPSF! UF VKIF L ZKCASYA FTD: FUYXFEFDH", "LEVIFZPHYRJUBSKMQATDCOWNGX"))

end = time.time()
print(end - start)