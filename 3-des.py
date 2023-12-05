from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

def pad(data):
    padding_length = 8 - (len(data) % 8)
    padded_data = data + bytes([padding_length] * padding_length)
    return padded_data

def unpad(data):
    padding_length = data[-1]
    if not all(byte == padding_length for byte in data[-padding_length:]):
        raise ValueError("Invalid padding")
    unpadded_data = data[:-padding_length]
    return unpadded_data

key1 = get_random_bytes(8)
key2 = get_random_bytes(8)
key3 = get_random_bytes(8)

cipher = DES3.new(key1 + key2 + key3, DES3.MODE_ECB)

plaintext = input("Enter plaintext: ")
plaintext_bytes = plaintext.encode("utf-8")

padded_plaintext = pad(plaintext_bytes)

ciphertext = cipher.encrypt(padded_plaintext)
encrypted_hex = ciphertext.hex()
encrypted_hex_clean = encrypted_hex.replace('/', '').replace('x', '')
print("Ciphertext:", encrypted_hex_clean)

decrypted_bytes = cipher.decrypt(ciphertext)
unpadded_plaintext = unpad(decrypted_bytes)

decrypted = unpadded_plaintext.decode("utf-8")
print("Decrypted:", decrypted)
