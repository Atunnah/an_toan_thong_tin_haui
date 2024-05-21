import math as m
import random

prime = []
N_MAX = 1000
p, q, n, fi, e, d = None, None, None, None, None, None

def sleve():
    nt = [True] * N_MAX
    nt[0] = nt[1] = False
    for i in range(2, m.isqrt(N_MAX) + 1) :
        if nt[i]:
            for j in range(i * i, N_MAX, i):
                nt[j] = False
    for i in range(2, N_MAX):
        if nt[i]:
            prime.append(i)

def randomPrime():
    k = prime[random.randint(2, len(prime) - 1)]     
    prime.remove(k)
    return k

def gcd(a, b):
    if b == 0: 
        return a
    else:
        return gcd(b, a % b)
    
def mod(a, b, c):
    decimal2binary = bin(b)[2:]
    f = 1
    for i in decimal2binary:
        f = (f * f) % c
        if i == '1':
            f = (f * a) % c
    return f

def inverseMod(a, b):
    for i in range(1, b):
        if ((a % b) * (i % b)) % b == 1:
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
    d = inverseMod(e, fi)

def encrypt(m):
    global e, n
    c = mod(m, e, n)
    return c

def encyptString(m):
    encode = []
    for i in m:
        encode.append(encrypt(ord(i)))
    return encode

def decrypt(c):
    global d, n
    m = mod(c, d, n)
    return m

def decyptString(encode):
    text = ""
    for i in encode:
        text += chr(decrypt(i))
    return text

sleve()
key()
m = input("Enter text: ")
encode = encyptString(m)
print("Encrypt code: ", encode)
print("Decrypt text: ", decyptString(encode))

