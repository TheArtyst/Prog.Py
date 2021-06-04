from hashlib import sha256

entree = input("Nom du fichier à chiffrement ou déchiffrement :")
sortie = input("Nom du fichier de sortie :")
cle = input("PassPhrase :")
cle_h = sha256(cle.encode('utf-8')).digest() # digest renvoie la clé sha dans la variable cle_h

with open(entree,'rb') as f_entree:  # open = ouvre le fichier rb = read binarie permet d'ouvrir le fichier au format binaire 
    with open(sortie,'wb') as f_sortie: # ouverture du fichier en ecriture binaire
        i = 0
        while f_entree.peek(): # .peek() renvoie l'élémént le plus haut de la pile soit ici le dernier octet du fichier
            c = ord(f_entree.read(1)) # f_entree.read(1) retourne un octet par octet le fichier sous forme de cc, ord permet de le passer en binaire
            j = i % len(cle_h) # permet de determiner quand la clé a était complétement lu (jusqu'a 256 ici puisque sha256)
            b = bytes([c^cle_h[j]]) # variable c XOR Clé_hashe à l'indice J donc premier caractére de la clé puis second etc...... XOR prend le permier bit de la clé et le premier bit du fichier à chiffrer et Le résultat est 1 si un et un seul des opérandes A et B est VRAI = 1  
            f_sortie.write(b)
            i = i + 1