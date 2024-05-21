def create_vietnamese_alphabet():
    # Tạo từ điển với các ký tự Tiếng Việt và dấu tương ứng
    vietnamese_alphabet = {
        'A': 'A', 'À': 'À', 'Á': 'Á', 'Ả': 'Ả', 'Ã': 'Ã', 'Ạ': 'Ạ',
        'Ă': 'Ă', 'Ằ': 'Ằ', 'Ắ': 'Ắ', 'Ẳ': 'Ẳ', 'Ẵ': 'Ẵ', 'Ặ': 'Ặ',
        'Â': 'Â', 'Ầ': 'Ầ', 'Ấ': 'Ấ', 'Ẩ': 'Ẩ', 'Ẫ': 'Ẫ', 'Ậ': 'Ậ',
        'B': 'B', 'C': 'C', 'D': 'D', 'Đ': 'Đ', 'E': 'E', 'È': 'È',
        'É': 'É', 'Ẻ': 'Ẻ', 'Ẽ': 'Ẽ', 'Ẹ': 'Ẹ', 'Ê': 'Ê', 'Ề': 'Ề',
        'Ế': 'Ế', 'Ể': 'Ể', 'Ễ': 'Ễ', 'Ệ': 'Ệ', 'F': 'F', 'G': 'G',
        'H': 'H', 'I': 'I', 'Ì': 'Ì', 'Í': 'Í', 'Ỉ': 'Ỉ', 'Ĩ': 'Ĩ',
        'Ị': 'Ị', 'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N',
        'O': 'O', 'Ò': 'Ò', 'Ó': 'Ó', 'Ỏ': 'Ỏ', 'Õ': 'Õ', 'Ọ': 'Ọ',
        'Ô': 'Ô', 'Ồ': 'Ồ', 'Ố': 'Ố', 'Ổ': 'Ổ', 'Ỗ': 'Ỗ', 'Ộ': 'Ộ',
        'Ơ': 'Ơ', 'Ờ': 'Ờ', 'Ớ': 'Ớ', 'Ở': 'Ở', 'Ỡ': 'Ỡ', 'Ợ': 'Ợ',
        'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 'U': 'U',
        'Ù': 'Ù', 'Ú': 'Ú', 'Ủ': 'Ủ', 'Ũ': 'Ũ', 'Ụ': 'Ụ', 'Ư': 'Ư',
        'Ừ': 'Ừ', 'Ứ': 'Ứ', 'Ử': 'Ử', 'Ữ': 'Ữ', 'Ự': 'Ự', 'V': 'V',
        'W': 'W', 'X': 'X', 'Y': 'Y', 'Ỳ': 'Ỳ', 'Ý': 'Ý', 'Ỷ': 'Ỷ',
        'Ỹ': 'Ỹ', 'Ỵ': 'Ỵ', 'Z': 'Z', 'a': 'a', 'à': 'à', 'á': 'á',
        'ả': 'ả', 'ã': 'ã', 'ạ': 'ạ', 'ă': 'ă', 'ằ': 'ằ', 'ắ': 'ắ',
        'ẳ': 'ẳ', 'ẵ': 'ẵ', 'ặ': 'ặ', 'â': 'â', 'ầ': 'ầ', 'ấ': 'ấ',
        'ẩ': 'ẩ', 'ẫ': 'ẫ', 'ậ': 'ậ', 'b': 'b', 'c': 'c', 'd': 'd',
        'đ': 'đ', 'e': 'e', 'è': 'è', 'é': 'é', 'ẻ': 'ẻ', 'ẽ': 'ẽ',
        'ẹ': 'ẹ', 'ê': 'ê', 'ề': 'ề', 'ế': 'ế', 'ể': 'ể', 'ễ': 'ễ',
        'ệ': 'ệ', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'ì': 'ì',
        'í': 'í', 'ỉ': 'ỉ', 'ĩ': 'ĩ', 'ị': 'ị', 'j': 'j', 'k': 'k',
        'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'ò': 'ò', 'ó': 'ó',
        'ỏ': 'ỏ', 'õ': 'õ', 'ọ': 'ọ', 'ô': 'ô', 'ồ': 'ồ', 'ố': 'ố',
        'ổ': 'ổ', 'ỗ': 'ỗ', 'ộ': 'ộ', 'ơ': 'ơ', 'ờ': 'ờ', 'ớ': 'ớ',
        'ở': 'ở', 'ỡ': 'ỡ', 'ợ': 'ợ', 'p': 'p', 'q': 'q', 'r': 'r',
        's': 's', 't': 't', 'u': 'u', 'ù': 'ù', 'ú': 'ú', 'ủ': 'ủ',
        'ũ': 'ũ', 'ụ': 'ụ', 'ư': 'ư', 'ừ': 'ừ', 'ứ': 'ứ', 'ử': 'ử',
        'ữ': 'ữ', 'ự': 'ự', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y',
        'ỳ': 'ỳ', 'ý': 'ý', 'ỷ': 'ỷ', 'ỹ': 'ỹ', 'ỵ': 'ỵ', 'z': 'z'
    }
    return vietnamese_alphabet

def caesar_cipher(text, shift):
    result = ''
    vietnamese_alphabet = create_vietnamese_alphabet()
    for char in text:
        if char in vietnamese_alphabet:
            shifted_char = vietnamese_alphabet[char]
            idx = (list(vietnamese_alphabet.keys())).index(char)
            new_idx = (idx + shift) % len(vietnamese_alphabet)
            result += (list(vietnamese_alphabet.keys()))[new_idx]
        else:
            result += char
    return result

# Ví dụ mã hóa văn bản Tiếng Việt 'Xin chào, Việt Nam!' với độ dịch là 3
text = input('Nhập vào đoạn cần mã hóa: ')
cnt = int(input('Số dịch: '))
encrypted_text = caesar_cipher(text, cnt)
print("Mã hóa:", encrypted_text)

# Ví dụ giải mã văn bản đã mã hóa trở lại
decrypted_text = caesar_cipher(encrypted_text, -cnt)
print("Giải mã:", decrypted_text)
