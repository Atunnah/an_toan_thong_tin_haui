import random
from math import pow

def is_prime(p):
    if p <= 1:
        return False
    if p <= 3:
        return True
    if p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i += 6
    return True

def random_prime():
    while True:
        p = random.randint(2, 100)
        if is_prime(p):
            return p
    
def gen_key(p):
    return random.randint(1, p - 1)

def power(a, b, p):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
        b = b >> 1
        a = a * a
    return res % p

def modInverse(a, p):
    for x in range(1, p):
        if ((a % p) * (x % p)) % p == 1:
            return x

def encrypt(p, a, y, M):
    # k = gen_key(p)
    k = 36
    key = power(y, k, p)
    c1 = power(a, k, p)
    c2 = []
    for c in M:
        a = ord(c)
        c_2 = (key * a) % p
        c2.append(c_2)
    # c2 = (key * M) % p
    print(f"{M} is encrypted: ", end='')
    print("{", c1, ", ", c2, "}")
    return c1, c2

def de(c1, c2):
    global x, p, key
    key = power(c1, x, p)
    m = (modInverse(key, p) * c2 % p) % p
    return m

def decrypt(p, x, c1, c2):
    # key = power(c1, x, p)
    # b = modInverse(key, p)
    M = ''
    for i in c2:
        # M += chr(((i % p) * b) % p)
        M += chr(de(c1, i))
    # M = (c2 * b) % p
    return M


# p = random_prime()
# a = random.randint(2, 100)
# x = random.randint(2, 100)

p, a, x = 97, 5, 58

y = power(a, x, p)

M_en = 'abcd'

c1, c2 = encrypt(p, a, y, M_en)

M_de = decrypt(p, x, c1, c2)
print(M_de)