from pwn import xor

string="label"
flag=''

for char in string:
  flag+=chr(ord(char) ^ 13)

print("crypto{%s}" % flag)


