# reference : https://www.hackthebox.com/blog/business-ctf-2022-400-curves-write-up
from Crypto.Util.number import long_to_bytes
from sage.all_cmdline import *
from pwn import *

p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc

def solveDL():
    b = randint(1, p)
    E = EllipticCurve(GF(p), [a, b])

    order = E.order()
    factors = prime_factors(order)

    valid = []
    for factor in factors:
        if factor <= 2**40:
            valid.append(factor)

    prime = valid[-1]
    G = E.gen(0) * int(order / prime)
    print("G's  type:", type(G))
    
    tmp_point = G.xy()
    tmp_x, tmp_y = str(tmp_point[0]), str(tmp_point[1])
    # print(f"Sending Gx: {tmp_x}")
    r.sendlineafter("Gx: ", str(tmp_x))
    r.sendlineafter("Gy: ", str(tmp_y))

    data = r.recvline()
    print("data: ",data)
    Q = eval(data)
    print("Q's  type:", type(Q))
    try:
        Q = E(Q[0], Q[1])
        print("Q's  type after E() :", type(Q))
        log = G.discrete_log(Q)
        print(f"DL found: {log}")
        return (log, prime)
    except Exception as e:
        print(e)
        return None, None


if __name__ == "__main__":
    dlogs = []
    pRimes = []
    for i in range(1, 16):
        r = remote("10.113.184.121", 10034)
        lOg, prime = solveDL()
        if lOg != None:
            dlogs.append(lOg)
            pRimes.append(prime)
        print(f"counter: {i}")
        r.close()
    super_secret = CRT_list(dlogs, pRimes)
    print(long_to_bytes(super_secret))
