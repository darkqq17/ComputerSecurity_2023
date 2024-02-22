from z3 import *

s = Solver()

bv = BitVec('bv', 8)
s.add(bv + 0x20 == 0x30)

if s.check() == sat:
    m = s.model()
    print(m)
    print(m[bv].as_long())
    