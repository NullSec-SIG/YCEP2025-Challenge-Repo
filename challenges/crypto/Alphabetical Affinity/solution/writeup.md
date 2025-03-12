# Alphabetical Affinity
In this challenge, participants are expected to reverse engineer a script to find the cipher used, the Affine Cipher.
They are to then create a decryption script based on the cipher and utilize the ciphertext (ciphertext.txt) and keys obtained (decoding 2V5cw==.txt) to obtain the plaintext.
The plaintext, `didyouknowthatmodinverseisinrsa` is to be encased with the flag format to obtain YCEP25{didyouknowthatmodinverseisinrsa}.

The participants are provided with 3 files:
- `encryption.py` (A file providing the script)
- `ciphertext.txt` (A text file containing the ciphertext)
- `a2V5cw==.txt` (A text file containing the keys in base64 encoding) 

In the solutions folder, a decryption script is provided.

The title and encryption script provides hints about the cipher utilized for encryption, the Affine Cipher.
Such hints include the use of the gcd() function from the math import, as well as the given modulo value and limitations of the plaintext.

```python
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

```
