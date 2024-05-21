from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    actual_ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded_text = cipher.decrypt(actual_ciphertext)
    decrypted_text = unpad(decrypted_padded_text, AES.block_size)
    
    return decrypted_text.decode()

# Example usage
key = get_random_bytes(16)  # AES-128 uses a 16-byte key

message = input("Enter message: ")

# Encrypt the message
encrypted_message = aes_encrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")

# Decrypt the message
decrypted_message = aes_decrypt(encrypted_message, key)
print(f"Decrypted Message: {decrypted_message}")
