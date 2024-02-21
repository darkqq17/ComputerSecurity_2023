from random import randint
from Crypto.Util.number import *
from hashlib import sha256
from ecdsa import SECP256k1
from ecdsa.ecdsa import Public_key, Private_key, Signature
from secret import FLAG

E = SECP256k1
G, n = E.generator, E.order

d = randint(1, n)
k = randint(1, n)
pubkey = Public_key(G, d*G)
prikey = Private_key(pubkey, d)
print(f'P = ({pubkey.point.x()}, {pubkey.point.y()})')

for _ in range(3):
    print('''
1) Request for Signature
2) Check the Permission
3) exit''')
    # 先要兩個簽章, 把ephemeral key消掉, 就可以得到d來自己製造簽章
    option = input()
    if option == '1':
        msg = input('What do you want? ')
        if msg == 'Give me the FLAG.': # 不簽特定訊息
                print('No way!')
        else:
            h = sha256(msg.encode()).digest()
            k = k * 1337 % n # 這題的問題在於這裡的k沒有很亂數產生, 是一個固定線性的乘上某個東西
            sig = prikey.sign(bytes_to_long(h), k)
            print(f'sig = ({sig.r}, {sig.s})')

    elif option == '2': 
        msg = 'Give me the FLAG.' # 目的 : 偽造出一個這樣message的signature
        r = input('r: ')
        s = input('s: ')
        h = bytes_to_long(sha256(msg.encode()).digest())
        verified = pubkey.verifies(h, Signature(int(r), int(s)))
        if verified:
            print(FLAG)
        else:
            print('Bad signature')
    else:
        print("bye~")
        break

