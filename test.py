# def encrypt(m, s):
#     encode = ''
#     for char in m:
#         if char.isalpha():
#             encode += chr((ord(char) + s) % 7929)
#         else:
#             encode += char
#     return encode

# def decrypt(m, s):
#     result = ''
#     for char in m:
#         if char.isalpha():
#             result += chr((ord(char) - s) % 7929)
#         else:
#             result += char
#     return result


# m = input("Enter message: ")
# s = int(input("Enter shift: "))
# encode = encrypt(m, s)
# print("Encrypted message: ", encode)
# print("Decrypted message: ", encrypt(encode, -s))

for i in range(ord('A'), ord('Z')):
    print(chr(i))
