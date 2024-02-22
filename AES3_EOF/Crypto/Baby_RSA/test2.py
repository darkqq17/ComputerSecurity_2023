from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import AES
from pwn import *
from sage.all import *

# Coppersmith's method to find small roots
def find_small_root(ciphertext, modulus, exponent):
    return 

# nc chal1.eof.ais3.org 10002
if __name__ == '__main__':
    r = remote('chal1.eof.ais3.org', 10002)
    print(r.recvline())
    print(r.recvline())
    r.recvuntil('FLAG:  ')
    flag_1 = r.recvline().strip()
    print("flag_1:", flag_1)
    r.sendlineafter('Any message for me?', flag_1)
    r.recvuntil('New Message:  ')
    flag_2 = r.recvline().strip()
    print("flag_2:", flag_2)
    r.sendlineafter('Any message for me?', flag_1)
    r.recvuntil('New Message:  ')
    flag_3 = r.recvline().strip()
    print("flag_3:", flag_3)
    r.interactive()