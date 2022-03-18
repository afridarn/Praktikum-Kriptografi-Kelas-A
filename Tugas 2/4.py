from pwn import xor

encrypted = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
format = "crypto{"

print(xor(encrypted,format.encode()))
guessed_key = "myXORkey"
print("key= myXORkey")
print(xor(guessed_key.encode(), encrypted))