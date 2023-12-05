p = 23  
a = 1   
b = 1   
G = (5, 19)  
n = 37  


def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def point_addition(p1, p2):
    if p1 is None:
        return p2
    x1, y1 = p1
    x2, y2 = p2

    if p1 == p2:
        s = ((3 * x1 * x1 + a) * mod_inverse(2 * y1, p)) % p
    else:
        s = ((y2 - y1) * mod_inverse(x2 - x1, p)) % p

    x3 = (s * s - x1 - x2) % p
    y3 = (s * (x1 - x3) - y1) % p
    return x3, y3


def scalar_multiply(k, point):
    if k == 0:
        return None  
    elif k == 1:
        return point  

    result = None
    for _ in range(k):
        if result is None:
            result = point
        else:
            result = point_addition(result, point)
    return result

alice_private_key = 6  
alice_public_key = scalar_multiply(alice_private_key, G)  


bob_private_key = 15  
bob_public_key = scalar_multiply(bob_private_key, G)  


alice_shared_secret = scalar_multiply(alice_private_key, bob_public_key)
bob_shared_secret = scalar_multiply(bob_private_key, alice_public_key)


print("Alice's shared secret:", alice_shared_secret)
print("Bob's shared secret:", bob_shared_secret)

