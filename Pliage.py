f = 0.0001 # épaisseur en mètres
t = 0 # Taille
nb = 0 # Nombre de pliage
while t < 324:
    nb = nb + 1
    t = f * 2**nb
    print(nb)
print("Nombre de pliage:",nb," hauteur:",t,"M")
