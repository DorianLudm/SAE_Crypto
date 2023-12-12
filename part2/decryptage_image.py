from PIL import Image

i = Image.open("./part2/img/rossignol1.bmp")
i2 = Image.open("./part2/img/rossignol2.bmp")
string_clé = ""
cpt = 0
counter_boucle = 0
for y in range(i.size[1]): #Colonne
    for x in range(i.size[0]): #Ligne
        counter_boucle += 1
        c_i = i.getpixel((x,y))
        c_i2 = i2.getpixel((x,y))
        if c_i == c_i2+1 or c_i == c_i2:
            string_clé += "0"
        else:
            cpt += 1
            string_clé += "1"
            print(counter_boucle, c_i, c_i2)
        if counter_boucle > 64:
            break
    if counter_boucle > 64:
        break
print(cpt)
print(string_clé)