possible_keys = [
    "encryption", "decryption", "cipher", "key", "algorithm", 
    "hashing", "plaintext", "ciphertext", "blockchain", "publickey", 
    "blowfish", "signature", "salting", "AES", "RSA", 
    "DiffieHellman", "HMAC", "SSL", "TLS", "hash", 
    "primitiveroot", "DHKE", "premasterkey", "fingerprinting", "token", 
    "pki", "vigenere", "random", "security", "generator", 
    "authentication", "symmetric", "asymmetric", "galoiscountermode", "salt", 
    "modularexponentiation", "XOR", "OR", "SHA", "MD5", 
    "confidentiality", "quantum", "maninmiddle", "multiplicativegroup", "protocol", 
    "integerfactorization", "message", "integrity", "keypair", "initializationvector", 
    "signature", "cryptanalysis", "plaintextattack", "discretelogarithm", "fuzzing", 
    "keyexchange", "password", "bruteforce", "salt", "PKI", 
    "publickeycryptography", "DES", "RNG", "cryptosystem", "substitution", 
    "permutation", "seed", "computationalpower", "lattice", "randomness", 
    "zeroknowledge", "cryptographic", "diffusion", "postquantum", "pairing", 
    "statevector", "hashcollision", "keyspace", "cyclicgroup", "secure", 
    "keysize", "ElGamal", "blockcipher", "enigma", "ciphersuite", 
    "substitutionbox", "cipherblockchaining", "hashfunction", "modulararithmetic", "quantumresistant", 
    "privatekey", "digitalcertificate", "onetimepad", "galoisfield", "ECC", 
    "railfencecipher", "Kuznyechik", "EllipticCurve", "Blake2b", "handshake"
]

def gen_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def dec(msg, key):
    decrypted_text = []
    key = gen_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('A'))
        elif char.islower():
            decrypted_char = chr((ord(char) - ord(key[i]) + 26) % 26 + ord('a'))
        else:
            decrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)

with open("enc.txt", "r") as f:
    ciphertext = f.read().strip()
    for key in possible_keys:
        decrypted_text = dec(ciphertext, key)
        print(f"Decrypted Text: {decrypted_text}")
        if "YCEP25" in decrypted_text:
            print(f"Key: {key}")
            print(f"Flag found: {decrypted_text}")
            break

