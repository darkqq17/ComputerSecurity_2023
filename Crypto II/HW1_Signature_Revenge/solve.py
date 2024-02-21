from Crypto.Util.number import *
from hashlib import sha256, md5
from ecdsa import SECP256k1
from sage.all import *

E = SECP256k1 # Elliptive Curve
G, n = E.generator, E.order # Generate generator and it's order
R = Integers(n)

sig1 = (26150478759659181410183574739595997895638116875172347795980556499925372918857, 50639168022751577246163934860133616960953696675993100806612269138066992704236)
sig2 = (8256687378196792904669428303872036025324883507048772044875872623403155644190, 90323515158120328162524865800363952831516312527470472160064097576156608261906)

h1 = sha256(b"https://www.youtube.com/watch?v=IBnrn2pnPG8").digest()
h2 = sha256(b"https://www.youtube.com/watch?v=1H2cyhWYXrE").digest()

h1, h2 = R(bytes_to_long(h1)), R(bytes_to_long(h2))
r1, r2 = R(sig1[0]), R(sig2[0])
s1, s2 = R(sig1[1]), R(sig2[1])

a = (2 ** 128) - s2*(r2**-1)*(s1**-1)*r1
t = -((a**-1) * ((2 ** 128) * s2 * (r2**-1) * (s1**-1) * r1 - 1))
u = (a **-1) * ((r2**-1)*(s1**-1)*r1*h2 - (s1**-1)*h1)

K = (1 << 128) - 1
print("K :", K)
# Step 2: Construct the Lattice
B = Matrix(ZZ, 3, 3, [[n, 0, 0], [t, 1, 0], [u, 0, K]])

# Step 3: LLL Reduction
B_reduced = B.LLL()

v1_m1, v1_m2, v1_Big_k = B_reduced[0]
print("Vector1 - m1: ", v1_m1, "m2: ", v1_m2, "Big K: ", v1_Big_k)
# print(m1.bit_length(), m2.bit_length())

v2_m1, v2_m2, v2_Big_k = B_reduced[1]
print("Vector2 - m1: ", v2_m1, "m2: ", v2_m2, "Big K: ", v2_Big_k)
# print(m1.bit_length(), m2.bit_length())

v3_m1, v3_m2, v3_Big_k = B_reduced[2]
print("Vector3 - m1: ", v3_m1, "m2: ", v3_m2, "Big K: ", v3_Big_k)
# print(m1.bit_length(), m2.bit_length())


def check_flag(m1, m2):
    # m1_bytes, m2_bytes = long_to_bytes(abs(m1)), long_to_bytes(abs(m2))
    m1_bytes, m2_bytes = R(abs(m1)), R(abs(m2))
    # k = bytes_to_long(m1_bytes + m2_bytes)
    k = (2 ** 128) * m1_bytes + m2_bytes
    # d = (k - (s1**-1)*h1) * (((s1**-1)*r1) **-1)
    d = s1*(r1**-1)*k - (r1**-1)*h1
    # print(long_to_bytes(int(d)))
    if b'FLAG' in long_to_bytes(int(d)):
        print("FLAG found:", long_to_bytes(int(d)))
        return True
    return False

found_flag = False
# Try to combine rows of the B_reduced matrix with the coefficients ranging from -1000 to 1000
for coef1 in range(-100, 100):
    for coef2 in range(-100, 100):
        for i in range(B_reduced.nrows()):
            for j in range(B_reduced.nrows()):
                m1, m2, _ = coef1 * B_reduced[i] + coef2 * B_reduced[j]
                # print(m1, m2)
                if check_flag(m1, m2):
                    found_flag = True
                    break
            if found_flag:
                break
        if found_flag:
            break
    if found_flag:
        break