import random
from sympy import isprime, mod_inverse

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    
    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break
    
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    e, n = pk
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(pk, ciphertext):
    d, n = pk
    decrypted = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    p = 101
    q = 103
    public_key, private_key = generate_keypair(p, q)
    
    message = input("Enter your message: ")
    encrypted_msg = encrypt(public_key, message)
    decrypted_msg = decrypt(private_key, encrypted_msg)
    
    print("Original message: ", message)
    print("Public key: ", public_key)
    print("Private key: ", private_key)
    print("Encrypted message: ", encrypted_msg)
    print("Decrypted message: ", decrypted_msg)

if __name__ == '__main__':
    main()
