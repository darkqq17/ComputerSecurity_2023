from pwn import *
from Crypto.Util.number import *
from hashlib import sha256
from ecdsa import SECP256k1
from ecdsa.ecdsa import Public_key, Private_key, Signature

r = remote('10.113.184.121', 10033)

# emphemeral key會換, 所以丟兩個一樣的message也可以拿到不一樣的signature
r.sendlineafter(b"3) exit\n", str(1).encode())
r.sendlineafter(b"What do you want? ", b"\(~_~)/")
r.recvuntil(b"sig = ")
r1, s1 = eval(r.recvline().decode())
print("r1 : ", r1, "s1 : ", s1)
h1 = bytes_to_long(sha256(b"\(~_~)/").digest())

r.sendlineafter(b"3) exit\n", str(1).encode())
r.sendlineafter(b"What do you want? ", b"\(~_~)/")
r.recvuntil(b"sig = ")
r2, s2 = eval(r.recvline().decode())
print("r2 : ", r2, "s2 : ", s2)
h2 = bytes_to_long(sha256(b"\(~_~)/").digest())

E = SECP256k1 # 某個elliptive curve的名字
G, n = E.generator, E.order

d = pow((r2 * pow(s2, -1, n) - 1337 * r1 * pow(s1, -1, n)), -1, n) * \
    (1337 * h1 * pow(s1, -1, n) - h2 * pow(s2, -1, n))
    
pubkey = Public_key(G, d * G)
prikey = Private_key(pubkey, d)

msg = 'Give me the FLAG.'
h = sha256(msg.encode()).digest()
k = 0xb09902017
sig = prikey.sign(bytes_to_long(h), k)
print("sig_r : ", sig.r)
print("sig_s : ", sig.s)
r.sendlineafter(b"3) exit\n", str(2).encode())
r.sendlineafter(b"r: ", str(sig.r).encode())
r.sendlineafter(b"s: ", str(sig.s).encode())
r.interactive()