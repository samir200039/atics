# # # Utils # # #

def ascii_to_bin(pt: str) -> str:
    output = ''

    for char in pt:
        bin_str = bin(ord(char))[2:]
        if len(bin_str) < 8:
            bin_str = '0'*(8 - len(bin_str)) + bin_str
        output += bin_str
    
    return output

def bin_to_ascii(pt: str) -> str:
    output = ''

    for i in range(0, len(pt), 8):
        output += chr(int(pt[i: i + 8], 2))
    
    return output

def map_string(string: str, table) -> str:
    output = [''] * (len(table) * len(table[0]))

    for i in range(len(table)):
        for j in range(len(table[0])):
            output[i * len(table[0]) + j] = str(string[table[i][j] - 1])
    
    return ''.join(output)


    


# # # Mapping Tables # # #

initial_p = [
    [58, 50, 42, 34, 26, 18, 10, 2],
    [60, 52, 44, 36, 28, 20, 12, 4],
    [62, 54, 46, 38, 30, 22, 14, 6],
    [64, 56, 48, 40, 32, 24, 16, 8],
    [57, 49, 41, 33, 25, 17, 9, 1],
    [59, 51, 43, 35, 27, 19, 11, 3],
    [61, 53, 45, 37, 29, 21, 13, 5],
    [63, 55, 47, 39, 31, 23, 15, 7]
]

final_p = [
    [40, 8, 48, 16, 56, 24, 64, 32],
    [39, 7, 47, 15, 55, 23, 63, 31],
    [38, 6, 46, 14, 54, 22, 62, 30],
    [37, 5, 45, 13, 53, 21, 61, 29],
    [36, 4, 44, 12, 52, 20, 60, 28],
    [35, 3, 43, 11, 51, 19, 59, 27],
    [34, 2, 42, 10, 50, 18, 58, 26],
    [33, 1, 41, 9, 49, 17, 57, 25]
]

exp_d = [
    [32, 1, 2, 3, 4, 5, 4, 5],
    [6, 7, 8, 9, 8, 9, 10, 11],
    [12, 13, 12, 13, 14, 15, 16, 17],
    [16, 17, 18, 19, 20, 21, 20, 21],
    [22, 23, 24, 25, 24, 25, 26, 27],
    [28, 29, 28, 29, 30, 31, 32, 1]
]

sbox_map = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

per_ch_1 = [
    [57, 49, 41, 33, 25, 17, 9],
    [1, 58, 50, 42, 34, 26, 18],
    [10, 2, 59, 51, 43, 35, 27],
    [19, 11, 3, 60, 52, 44, 36],
    [63, 55, 47, 39, 31, 23, 15],
    [7, 62, 54, 46, 38, 30, 22],
    [14, 6, 61, 53, 45, 37, 29],
    [21, 13, 5, 28, 20, 12, 4]
]

per_ch_2 = [
    [14, 17, 11, 24, 1, 5, 3, 28],
    [15, 6, 21, 10, 23, 19, 12, 4],
    [26, 8, 16, 7, 27, 20, 13, 2],
    [41, 52, 31, 37, 47, 55, 30, 40],
    [51, 45, 33, 48, 44, 49, 39, 56],
    [34, 53, 46, 42, 50, 36, 29, 32]
]

straight_p = [
    [16, 7, 20, 21],
    [29, 12, 28, 17],
    [1, 15, 23, 26],
    [5, 18, 31, 10],
    [2, 8, 24, 14],
    [32, 27, 3, 9],
    [19, 13, 30, 6],
    [22, 11, 4, 25]
]

round = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# # # Main # # #

def cipher(pt: str, key: str, use_for_decipher: bool) -> str:
    subkeys = key_maker(ascii_to_bin(key))
    if use_for_decipher:
        subkeys = reversed(subkeys)

    pt = initial_permute(ascii_to_bin(pt))
    left, right = pt[:len(pt) // 2], pt[len(pt) // 2:]

    for subkey in subkeys:
        res = expansion_p(right)
        res = xor(res, subkey)
        res = sbox(res)
        res = straight_permute(res)
        res = xor(res, left)

        left = right
        right = res
    
    return bin_to_ascii(final_permute(right + left))



# # # Initial & Final permutes # # #

def initial_permute(bits: str) -> str:
    return map_string(bits, initial_p)

def final_permute(bits: str) -> str:
    return map_string(bits, final_p)



# # # Round Logic # # #

def expansion_p(bits: str):
    return map_string(bits, exp_d)

def xor(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        raise ValueError('XOR values have non equal sizes')
    
    output = ''
    for i in range(len(str1)):
        output += '0' if str1[i] == str2[i] else '1'
    return output

def sbox(bits: str) -> str:
    if len(bits) != 48:
        raise ValueError('48 bits required')
    
    output = ''
    for i in range(0, 48, 6):
        chosen = bits[i:i + 6]
        row = int(chosen[0] + chosen[-1], 2)
        col = int(chosen[1:-1], 2)

        num = bin(sbox_map[i // 6][row][col])[2:]
        if len(num) < 4:
            num = '0'*(4 - len(num)) + num
        
        output += num
    
    return output
    

def straight_permute(bits: str) -> str:
    return map_string(bits, straight_p)



# # # Key Operations # # #

def key_maker(key_64: str):
    key_56 = permute_choice_1(key_64)
    subkeys = []

    c, d = key_56[:len(key_56) // 2], key_56[len(key_56) // 2:]
    for i in range(16):
        for _ in range(round[i]):
            c = key_left_shift(c)
            d = key_left_shift(d)

            subkeys.append(permute_choice_2(c + d))
    
    return tuple(subkeys)


def permute_choice_1(key: str) -> str:
    return map_string(key, per_ch_1)

def permute_choice_2(key: str) -> str:
    return map_string(key, per_ch_2)

def key_left_shift(key: str):
    return key[1:] + key[0]


if __name__ == '__main__':
    pt = input('Enter plain text (only 8 characters allowed, further will be truncated): ')[:8]
    if len(pt) < 8:
        pt += 'X'*(8 - len(pt))
    key = input('Enter key (only 8 characters allowed, further will be truncated): ')[:8]
    if len(key) < 8:
        key += 'X'*(8 - len(key))

    ct = cipher(pt, key, False)
    print('Cipher text: ' + ct)
    print('Deciphered text: ' + cipher(ct, key, True))