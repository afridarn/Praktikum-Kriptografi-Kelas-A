from unittest import result
from pwn import xor

givendata = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
flag=''

for char in range(256):
   temp = [chr(n^char) for n in givendata]
   flag = "".join(temp)
   if flag.startswith("crypto"):
    print(flag)
