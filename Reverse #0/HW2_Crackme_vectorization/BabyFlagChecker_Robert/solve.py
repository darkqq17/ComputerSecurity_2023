import numpy as np
import base64
from Crypto.Util.number import long_to_bytes

src = np.array([[213, 150, 144, 217,  57, 140, 196],
 [ 50, 204, 156, 239, 239, 119, 100],
 [  5,  98, 135, 220,  47, 165,  24],
 [232,   6,  83,  52, 195,   4,  64],
 [219,  35, 114, 190, 210, 114,  94],
 [109,  43,  75, 136, 160, 230,  96],
 [ 15, 180, 224,  20, 125,  94,  85]]
)

s2 = np.array([[ 91834, 100005, 105865,  96406, 100532,  95980,  60737],
 [ 93214,  94177, 103788, 108760,  96189,  99044,  62768],
 [ 50987,  59054,  62968,  66175,  63413,  61405,  43979],
 [ 61719,  60974,  68003,  53197,  54398,  61283,  37530],
 [ 85810,  92042, 100303,  83377,  86292,  91469,  58351],
 [ 73600,  79743,  83593,  69477,  74716,  74583,  49541],
 [ 63447,  57246,  61636,  75652,  65751,  59280,  40038]])

# a * intput = b, input = a^-1 * b
input = np.round(np.dot(np.linalg.inv(src), s2)).astype(int)

print(49)
# print input matrix one by one
for i in range(7):
    for j in range(7):
        print(input[i][j])
        
# print input in base64 format
RevGuard = ''.join((long_to_bytes(int(i)).decode() for i in input.flatten()))
print(RevGuard)