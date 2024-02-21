from sage.all import *
from Crypto.Util.number import isPrime, getPrime, long_to_bytes
from random import choice
from pwn import *

N = 2
while True:
    bitLen = N.bit_length()
    if bitLen > 1024:
        N = 2
    if bitLen == 1024:
        if isPrime(N+1): 
            print(N+1)
            break
    N *= getPrime(10)
    
g = 7
r = remote('10.113.184.121', 10032)
r.sendlineafter(b"give me a prime: ", str(N+1).encode())
r.sendlineafter(b"give me a number: ", str(g).encode())
ret = r.recvline().decode()
m = int(ret.lstrip("The hint about my secret: "))
FLAG = discrete_log( Mod(m, N+1), Mod(g, N+1))
# print(m, g, FLAG)
print(long_to_bytes(FLAG))