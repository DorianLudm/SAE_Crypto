from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import time

data = b'secret data'

key = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
cipher = AES.new(key, AES.MODE_EAX, cipher.nonce)
debut = time.time()
data = cipher.decrypt_and_verify(ciphertext, tag)
fin = time.time()
temps = fin-debut
print("Temps de déchiffrement : ", temps)
print("Temps pour déchiffrer 2**128 messages : ", temps*2**128/3600/24/365, " ans")

print(data.decode("utf-8"))
