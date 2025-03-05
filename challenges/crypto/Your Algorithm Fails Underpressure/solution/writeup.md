Use YAFU to find p and q from n, then use this code:

```python
from sympy import mod_inverse

n = 102875787968861449238573685236444727881920554731721399500429101141646613741119
e = 65537  # Standard RSA public exponent

p = 316035022244213453167385335569272305847
q = 325520213672284186851544710661893934777

phi = (p - 1) * (q - 1)

d = mod_inverse(e, phi)

with open("message.enc", "rb") as f:
    encrypted_message = int.from_bytes(f.read(), byteorder="big")

decrypted_message = pow(encrypted_message, d, n)

try:
    plaintext = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder="big").decode()
    print("Decrypted Message:", plaintext)
except:
    print("Decryption failed. Try manually checking the output.")
