import requests

BASE_URL = "http://aes.cryptohack.org/block_cipher_starter"

#mengambil cipher text
r = requests.get(f"{BASE_URL}/encrypt_flag")
data = r.json()
ciphertext = data["ciphertext"]
print("ciphertext", ciphertext)

#melakukan decryption
r = requests.get(f"{BASE_URL}/decrypt/{ciphertext}")
data = r.json()
plaintext = data["plaintext"]
print("plaintext", plaintext)

#print flag
print("flag", bytearray.fromhex(plaintext).decode())