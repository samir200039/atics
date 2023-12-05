def power_mod(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

def diffie_hellman(p, g, private_key):
    public_key = power_mod(g, private_key, p)
    return public_key

def shared_secret(public_key, private_key, p):
    return power_mod(public_key, private_key, p)

p = 16633 #23
g = 29 #5

private_key_a = int(input("Enter secret of A: "))
private_key_b = int(input("Enter secret of B: "))

public_key_a = diffie_hellman(p, g, private_key_a)
public_key_b = diffie_hellman(p, g, private_key_b)

shared_secret_a = shared_secret(public_key_b, private_key_a, p)
shared_secret_b = shared_secret(public_key_a, private_key_b, p)

print("Public Key A: ", public_key_a)
print("Public Key B: ", public_key_b)
print("Shared Secret A: ", shared_secret_a)
print("Shared Secret B: ", shared_secret_b)