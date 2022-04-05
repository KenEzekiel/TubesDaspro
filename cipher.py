# This cipher uses the Affine Cipher.
import standard

def encrypt(password: str) -> str:
    """
    Encrypts user password using the Affine cipher.
    """

    # Hardcoded key
    a = 17
    b = 9
    ciphered = ''
    
    # e(x) = (ax + b) mod m
    for char in password:

        if 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90:
            if standard.is_lower(char):
                ciphered += chr(((a * (ord(char) - 97) + b) % 26) + 97)
            else:  # standard.is_upper(char)
                ciphered += chr(((a * (ord(char) - 65) + b) % 26) + 65)

        else:
            ciphered += char

    return ciphered

def decrypt(ciphered: str) -> str:
    """
    Decrypts ciphered user password using the Affine cipher.
    """
    a = 17
    b = 9
    i = 0
    password = ''

    # Finding a^(-1) which is the multiplicative inverse of a
    multiplicative_inverse = None
    while multiplicative_inverse is None:
        if ((i * 26) + 1) / a == ((i * 26) + 1) // a:
            multiplicative_inverse = int(((i * 26) + 1) / a)
            break
        else:
            i += 1
    
    # d(x) = a^(-1)(x - b) mod m
    for char in ciphered:

        if 97 <= ord(char) <= 122 or 65 <= ord(char) <= 90:
            if standard.is_lower(char):
                password += chr(((multiplicative_inverse * ((ord(char) - 97) - b)) % 26) + 97)
            else:  # standard.is_upper(char)
                password += chr(((multiplicative_inverse * ((ord(char) - 65) - b)) % 26) + 65)

        else:
            password += char

    return password
