from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def ibe_user_registration(master_key, user_id):
    private_key = master_key  
    return private_key


def ibe_encrypt(public_params, user_id, message):
    
    private_key = ibe_user_registration(public_params['master_key'], user_id)
    cipher = AES.new(private_key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode())
    return ciphertext, nonce, tag


def ibe_decrypt(private_key, ciphertext, nonce, tag):
    cipher = AES.new(private_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext.decode()


def ibs_user_registration(master_key, user_id):
    private_key = ECC.generate(curve='P-256')
    public_key = private_key.public_key()
    return private_key, public_key


def ibs_sign(private_key, message):
    h = SHA256.new(message.encode())
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(h)
    return signature


def ibs_verify(public_key, message, signature):
    h = SHA256.new(message.encode())
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False


master_key = get_random_bytes(16)
public_params = {'master_key': master_key}


user_id = "alice"
private_key_ibe = ibe_user_registration(master_key, user_id)
private_key_ibs, public_key_ibs = ibs_user_registration(master_key, user_id)


message = "I am inevitable"


ciphertext, nonce, tag = ibe_encrypt(public_params, user_id, message)


decrypted_message = ibe_decrypt(private_key_ibe, ciphertext, nonce, tag)


signature = ibs_sign(private_key_ibs, message)


is_valid_signature = ibs_verify(public_key_ibs, message, signature)


print("Decrypted Message:", decrypted_message)
print("Is Signature Valid?", is_valid_signature)
