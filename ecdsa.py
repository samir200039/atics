import random


prime = 23
a = 1
b = 1
Gx = 5
Gy = 19


def point_add(p, q, prime):
    if p is None:
        return q
    if q is None:
        return p
    x1, y1 = p
    x2, y2 = q
    if p != q:
        s = ((y2 - y1) * pow(x2 - x1, prime - 2, prime)) % prime
    else:
        s = ((3 * x1 * x1) * pow(2 * y1, prime - 2, prime)) % prime
    x3 = (s * s - x1 - x2) % prime
    y3 = (s * (x1 - x3) - y1) % prime
    return x3, y3


def scalar_mult(k, point, prime):
    result = None
    
    for i in range(min(k, 10)):  
        result = point_add(result, point, prime)
    return result



k = random.randint(1, 10)
print("Scalar (k):", k)


base_point = (Gx, Gy)
print("Base Point:", base_point)


result = scalar_mult(k, base_point, prime)
print("Result of Scalar Multiplication (limited steps):", result)

