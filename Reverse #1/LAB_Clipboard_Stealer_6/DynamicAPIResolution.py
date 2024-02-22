def rol(value, shift_bits, bit_size):
    max_value = (2 ** (bit_size) - 1) 
    return (value << shift_bits) | (value >> (bit_size - shift_bits)) & max_value

with open("./user32.dll.txt", 'rb') as f:
    names = f.read().split(b'\n')
    
for name in names:
    name = name.strip()
    h = 0
    for i in range(len(name)):
        h += rol(h, 11, 32) + 1187 + name[i]
        h = h & (2**(32) - 1)
    if h == 0x416f607:
        print(name)
        break