from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    """求取模逆元"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def chinese_remainder_theorem(n, a):
    """n 為模數的列表, a 為同餘式右邊的列表"""
    sum = 0
    prod = 1
    for ni in n:
        prod *= ni

    for ni, ai in zip(n, a):
        p = prod // ni
        sum += ai * modinv(p, ni) * p
    return sum % prod

# 根據你提供的資訊
hint = [2905235671, 766735348, 3064232839, 658990064, 403123940, 2153333672, 2359312739, 936290586, 3051250662, 2204499101, 1634715264, 2294459036, 574253990, 1046268858, 733510084, 380632133, 189664137, 1044146672, 460935278, 1590531285]
muls = [1005581, 773317, 828007, 697579, 750457, 949987, 753647, 1013833, 934187, 865957, 554207, 526381, 843397, 541483, 569021, 531793, 611323, 654767, 574529, 965267]
mods = [3904069501, 2369156627, 3650034217, 2593714229, 2718164573, 2892165043, 3996747731, 3516579067, 3256996537, 4126333501, 2342206099, 2575134977, 2371832579, 3664145747, 3689178683, 2766400097, 2280138979, 2927570389, 3660723839, 2542110731]

# 計算 a，它是 hint[i] / muls[i] % mods[i]
a = [(hint[i] * modinv(muls[i], mods[i])) % mods[i] for i in range(20)]

secret = chinese_remainder_theorem(mods, a)
print(long_to_bytes(secret))
