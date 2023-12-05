def left_rotate(value, shift):
    return ((value << shift) | (value >> (32 - shift))) & 0xFFFFFFFF

def sha1(text):
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    original_length = len(text) * 8
    text += b'\x80'
    while (len(text) % 64) != 56:
        text += b'\x00'
    text += original_length.to_bytes(8, byteorder='big')

    for i in range(0, len(text), 64):
        chunk = text[i:i + 64]

        words = [0] * 80
        for j in range(16):
            words[j] = int.from_bytes(chunk[j * 4:j * 4 + 4], byteorder='big')

        for j in range(16, 80):
            words[j] = left_rotate(words[j - 3] ^ words[j - 8] ^ words[j - 14] ^ words[j - 16], 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        for j in range(80):
            if j < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif j < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif j < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = left_rotate(a, 5) + f + e + k + words[j] & 0xFFFFFFFF
            e = d
            d = c
            c = left_rotate(b, 30)
            b = a
            a = temp

        h0 = (h0 + a) & 0xFFFFFFFF
        h1 = (h1 + b) & 0xFFFFFFFF
        h2 = (h2 + c) & 0xFFFFFFFF
        h3 = (h3 + d) & 0xFFFFFFFF
        h4 = (h4 + e) & 0xFFFFFFFF

    return '{:08x}{:08x}{:08x}{:08x}{:08x}'.format(h0, h1, h2, h3, h4)

if __name__ == "__main__":
    input_text = input("Enter the text: ")
    sha1_hash = sha1(input_text.encode())
    print("SHA-1 Hash:", sha1_hash)