from elliptic_curve import Curve, Point
from Crypto.Util.number import bytes_to_long
from secret import FLAG

# NIST P-256
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
n = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551 #order of the curve

print("Give me a G and I will give you the hint.")
E = Curve(p, a, b) #Create Elliptive Curve
Gx = int(input("Gx: "))
Gy = int(input("Gy: ")) # Give an G(x,y) on Curve E
G = Point(E, Gx, Gy)
hint = G * bytes_to_long(FLAG)
print(hint)