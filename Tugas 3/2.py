def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b, a%b)


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

print(egcd(26513, 32321))