import math as m
import random

N_Max = 1000
prime = []
p, q, n, fi, e, d = None, None, None, None, None, None

def sleve():
    nt = [True] * N_Max
    nt[0] = nt[1] = False
    for i in range(2, m.isqrt(N_Max) + 1):
        if nt[i]:
            for j in range(i * i, N_Max, i):
                nt[j] = False
    for i in range(2, N_Max):
        if nt[i]:
            prime.append(i)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)            

def randomPrime():
    global prime
    k = prime[random.randint(2, len(prime) - 1)]            
    prime.remove(k)
    return k

def mod(a, b, c):
    decimal2binary = bin(b)[2:]
    f = 1
    for i in decimal2binary:
        f = (f * f) % c
        if i == '1':
            f = (f * a) % c
    return f

def inverseMode(a, b):
    for i in range(1, b):
        if((a % b) * (i % b)) % b == 1:
            return i
        
def key():
    global p, q, n, fi, e, d
    p = randomPrime()
    q = randomPrime()
    n = p * q
    fi = (p - 1) * (q - 1)
    for i in range(2, fi):
        if gcd(i, fi) == 1:
            e = i
            break
    d = inverseMode(e, fi)

def encrypt(m):
    global n, e
    return mod(m, e, n)

def encryptString(m):
    encode = []
    for i in m:
        encode.append(encrypt(ord(i)))
    return encode

def decrypt(c):
    global n, d
    return mod(c, d, n)

def decryptString(c):
    text = ''
    for i in c:
        text += chr(decrypt(i))
    return text

sleve()
key()
m = input("Enter message: ")
encode = encryptString(m)
print("Encrypted code: ", encode)
print("Decrypted message: ", decryptString(encode))