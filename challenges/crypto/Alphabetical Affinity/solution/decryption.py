# function finds the modulo inverse of a
def mod_inverse(a: int, modulo: int) -> int or None:
    for x in range(1, modulo):
        if (a * x) % modulo == 1:
            return x
    return None


# main function for decryption
def decrypt():
    ciphertext: str = input("Enter the ciphertext to decrypt (Encase this with the YCEP25{} flag format): ")

    keys: str = input("Enter the keys of the cipher (Format: a, b): ")
    keys_list: list[int, int] = [int(k) for k in keys.strip().split(", ")]

    a, b = keys_list[0], keys_list[1]
    modulo: int = 26

    a_inv: int = mod_inverse(a, modulo)
    if a_inv is None:
        raise ValueError("No modulo inverse was found for key value a")

    # Note: (C - b) applies first before multiplication with the mod inverse in decryption
    #
    #                                   Applies first before a_inv
    #                                      VVVVVVVVVVVVVVVVVVVV
    plaintext: str = "".join([chr((a_inv * ((ord(t) - 65) - b)) % modulo + 65) for t in ciphertext.upper()])
    print("Plaintext:", plaintext)


decrypt()

