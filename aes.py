from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import base64


from  pycryptodome.lib.Crypto.Cipher import AES,
# from  pycryptodome.
 
def generate_key_and_iv(password, salt):
    key = PBKDF2(password, salt, dkLen=32, count=1000000)
    iv = get_random_bytes(16)
    return key, iv

def encrypt(plaintext, password):
    salt = get_random_bytes(16)
    key, iv = generate_key_and_iv(password.encode(), salt)
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    
    encrypted_data = salt + iv + ciphertext
    return base64.b64encode(encrypted_data).decode()

def decrypt(ciphertext, password):
    ciphertext = base64.b64decode(ciphertext)
    salt = ciphertext[:16]
    iv = ciphertext[16:32]
    ciphertext = ciphertext[32:]
    
    key, _ = generate_key_and_iv(password.encode(), salt)
    
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    
    return decrypted_data.decode()


# MAIN #
password = input("Enter key: ")
plaintext = input("Enter plain text: ")


encrypted_data = encrypt(plaintext.encode(), password)
print("Encrypted text: ", encrypted_data)


decrypted_data = decrypt(encrypted_data, password)
print("Decrypted text: ", decrypted_data)
