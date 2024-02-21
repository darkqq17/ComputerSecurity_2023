# Re-implementing the code after the execution state reset

# Mapping of case index to ASCII values as per the given code snippet
case_to_ascii = {
    0: 112,  # 'p'
    0x20: 112,  # 'p'
    1: 105,  # 'i'
    2: 110,  # 'n'
    3: 103,  # 'g'
    4: 123,  # '{'
    5: 122,  # 'z'
    6: 49,  # '1'
    9: 49,  # '1'
    7: 71,  # 'G'
    8: 95,  # '_'
    0xB: 95,  # '_'
    0x10: 95,  # '_'
    0x15: 95,  # '_'
    0xA: 83,  # 'S'
    0xC: 118,  # 'v'
    0xD: 51,  # '3'
    0x17: 51,  # '3'
    0xE: 82,  # 'R'
    0xF: 89,  # 'Y'
    0x11: 67,  # 'C'
    0x12: 48,  # '0'
    0x13: 79,  # 'O'
    0x1E: 79,  # 'O'
    0x14: 108,  # 'l'
    0x21: 108,  # 'l'
    0x16: 50,  # '2'
    0x1F: 50,  # '2'
    0x18: 52,  # '4'
    0x19: 109,  # 'm'
    0x1A: 75,  # 'K'
    0x1C: 75,  # 'K'
    0x1B: 73,  # 'I'
    0x1D: 73,  # 'I'
    0x22: 125,  # '}'
}

# Sorting the keys (case indexes) to ensure correct order
sorted_keys = sorted(case_to_ascii.keys())

# Constructing the flag from the sorted keys
flag = ''.join([chr(case_to_ascii[k]) for k in sorted_keys])

print(flag)