from PIL import Image

def comparaison_img(img1, img2):
    # On retourne ici la clé sur 64 bits, mais la clé est print sur 128 bits dans le terminal afin de montrer que celle-ci est bien coder sur les 64 premiers bits
    i = Image.open(img1)
    i2 = Image.open(img2)
    string_clé = ""
    cpt = 0
    counter_boucle = 0
    for y in range(i.size[1]): #Colonne
        for x in range(i.size[0]): #Ligne
            counter_boucle += 1
            c_i2 = i2.getpixel((x,y))
            string_clé += str(c_i2%2)
            if counter_boucle >= 128:
                break
        if counter_boucle >= 128:
            break
    print(cpt, string_clé)
    return string_clé[0:64]

key = comparaison_img("./part2/img/rossignol1.bmp", "./part2/img/rossignol2.bmp")