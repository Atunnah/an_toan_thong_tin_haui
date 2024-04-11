def caesar(s, shift):
    result = ""
    for char in s:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)
    return result

s = input("Nhap chuoi can ma hoa: ")
shift = int(input("Nhap so buoc: "))
print("Chuoi sau khi ma hoa: ", caesar(s, shift))