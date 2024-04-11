# (a * x) mod m = 1
def modInverse(a, m):
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
        
a = int(input("Nhap a: "))
m = int(input("Nhap m: "))
print("x = ", modInverse(a, m))