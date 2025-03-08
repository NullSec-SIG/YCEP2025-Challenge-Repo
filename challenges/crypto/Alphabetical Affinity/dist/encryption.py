from math import gcd


def encrypt():
    plaintext: str = input("Enter the plaintext to encrypt (ONLY include alphabets): ")
    if plaintext.isalpha() is False:
        raise ValueError("Plaintext is not in its valid format")

    keys: str = input("Enter the keys of the cipher (Format: a, b): ")
    try:
        keys_list: list[int, int] = [int(k) for k in keys.strip().split(", ")]
        if len(keys_list) != 2:
            raise ValueError("Keys are not in the valid format of: a, b")

    except ValueError:
        raise ValueError("The keys are integers, maybe they need to be decoded first?")

    except TypeError:
        raise ValueError("Keys are not in the valid format of: a, b")

    a, b = keys_list[0], keys_list[1]
    modulo: int = 26

    result: int = gcd(a, modulo)
    if result != 1:
        raise ValueError("One of the keys is not coprime with the modulo of 26")

    ciphertext: str = "".join([chr((a * (ord(t) - 65) + b) % modulo + 65) for t in plaintext.upper()])
    print("Ciphertext:", ciphertext)


encrypt()

