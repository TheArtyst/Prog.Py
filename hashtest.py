from hashlib import sha256

cle = "ftg"

Cle_Hashe = sha256(cle.encode('utf-8')).digest()

print(Cle_Hashe)