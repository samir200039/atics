def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def md5(text):
    a = 0x67452301
    b = 0xEFCDAB89
    c = 0x98BADCFE
    d = 0x10325476

    original_length = len(text) * 8
    text += b'\x80'
    while (len(text) % 64) != 56:
        text += b'\x00'
    text += original_length.to_bytes(8, byteorder='little')

    for i in range(0, len(text), 64):
        chunk = text[i:i + 64]

        words = [0] * 16
        for j in range(16):
            words[j] = int.from_bytes(chunk[j * 4:j * 4 + 4], byteorder='little')

        aa, bb, cc, dd = a, b, c, d

        for j in range(64):
            if j < 16:
                f = (b & c) | ((~b) & d)
                g = j
            elif j < 32:
                f = (d & b) | ((~d) & c)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = b ^ c ^ d
                g = (3 * j + 5) % 16
            else:
                f = c ^ (b | (~d))
                g = (7 * j) % 16

            temp = d
            d = c
            c = b
            b = (b + left_rotate((a + f + words[g] + 0x5A827999) & 0xFFFFFFFF, 7)) & 0xFFFFFFFF
            a = temp

        a = (a + aa) & 0xFFFFFFFF
        b = (b + bb) & 0xFFFFFFFF
        c = (c + cc) & 0xFFFFFFFF
        d = (d + dd) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}'.format(a, b, c, d)

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    md5_hash = md5(input_text.encode())
    print("MD5 Hash:", md5_hash)
