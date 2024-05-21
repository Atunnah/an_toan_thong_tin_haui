import math as m
import random

N_MAX = 10000001
p, a, x, k, K, C1, C2 = None, None, None, None, None, None, None
prime = []

def sleve():
    global prime
    nt = [True] * N_MAX
    nt[0] = nt[1] = False
    for i in range(2, m.isqrt(N_MAX) + 1):
        if nt[i]:
            for j in range(i * i, N_MAX, i):
                nt[j] = False
    for i in range(2, N_MAX):
        if nt[i]:
            prime.append(i)

def randomPrime():
    global prime
    return prime[random.randint(2, len(prime) - 1)]

def randomNumber():
    return random.randint(1, 2000)

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
        if((a % b) * (i % b)) % b == 1:
            return i
        
def key():
    global p, a, x, y, k
    p = randomPrime()
    a = randomNumber()
    x  = randomNumber()
    y = mod(a, x, p)
    k = random.randint(1, p - 1)

def encrypt(m):
    global p, a, x, y, k, K, C1, C2
    K = mod(y, k, p)
    C1 = mod(a, k, p)
    C2 = (K * m) % p
    return [C1, C2]

def encryptString(m):
    encode = []
    for i in m:
        encode.append(encrypt(ord(i)))
    return encode

def decrypt(c):
    global p, a, x, y, K, C1, C2
    C1, C2 = c
    K = mod(C1, x, p)
    M = (inverseMod(K, p) * (C2 % p)) % p
    return M

def decryptString(c):
    text = ''
    for i in c:
        text += chr(decrypt(i))
    return text

sleve()
key()
m = input("Enter message: ")
encode = encryptString(m)
print("Encrypted Code: ", encode)
print("Decrypted Message: ", decryptString(encode))