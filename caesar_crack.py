def encrypt(pt, key):
    output = ''
    offset = 0

    for char in pt:
        if 65 <= ord(char) < 65 + 26:
            offset = 65
        else:
            offset = 97

        output += chr((((ord(char) - offset) + key + 26) % 26) + offset)
    
    return output

def crack(ct, pt):
    for key in range(26):
        output = ''
        offset = 0
        for char in ct:
            if 65 <= ord(char) < 65 + 26:
                offset = 65
            else:
                offset = 97

            output += chr((((ord(char) - offset) - key + 26) % 26) + offset)
        if output == pt:
            return (key, output)

pt = input('Enter message: ')
key = int(input('Enter key: '))

ct = encrypt(pt, key)
print('Encrypted text: ', ct)

(cracked_key, cracked_message) = crack(ct, pt)
print('Cracked key: ', cracked_key)
print('Cracked message: ', cracked_message)