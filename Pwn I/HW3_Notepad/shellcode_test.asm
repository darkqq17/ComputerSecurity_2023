section .text
global _start

_start:
    ; Create a socket with domain AF_INET (IPv4 Internet protocols) and type SOCK_STREAM (TCP)
    xor rax, rax        ; Clear rax register
    mov al, 0x29        ; Syscall number for socket creation in x64

    xor rdi, rdi        ; Clear rdi register
    mov dil, 0x2        ; Set rdi to AF_INET (2)

    xor rsi, rsi        ; Clear rsi register
    mov sil, 0x1        ; Set rsi to SOCK_STREAM (1)

    xor rdx, rdx        ; Clear rdx register (Protocol is set to 0)

    syscall             ; Perform syscall to create the socket
    mov r8, rax         ; Save the socket file descriptor in r8 for later use

    ; Connect the socket to 127.0.0.1:8765
    xor rax, rax        ; Clear rax register
    mov al, 0x2a        ; Syscall number for connect in x64

    mov rdi, r8         ; Set rdi to the socket file descriptor

    mov rsi, 0xffffffffffffffff ; Prepare rsi for sockaddr struct
    mov r9, 0xfeffff80c2ddfffd  ; Prepare r9 for subtraction 
    sub rsi, r9        ; Calculate sockaddr struct with IP and port
    push rsi           ; Push sockaddr struct onto stack
    mov rsi, rsp       ; Set rsi to point to the sockaddr struct on stack

    xor rdx, rdx       ; Clear rdx register
    mov dl, 0x10       ; Set rdx to sizeof(struct sockaddr) (16 bytes)

    syscall            ; Perform syscall to connect the socket

    ; Send a command through the socket
    xor r9, r9         ; Clear r9 register
    mov r9w, 0x8787    ; Set command (0x8787) to send
    push r9            ; Push command onto stack

    xor rax, rax       ; Clear rax register
    mov al, 0x1        ; Syscall number for write in x64

    mov rdi, r8        ; Set rdi to the socket file descriptor

    mov rsi, rsp       ; Set rsi to point to the command on stack

    xor rdx, rdx       ; Clear rdx register
    mov dl, 0xa4       ; Set rdx to the size of the command

    syscall            ; Perform syscall to send the command

    ; Read response from the socket
    xor rax, rax       ; Clear rax register

    mov rdi, r8        ; Set rdi to the socket file descriptor

    mov rsi, rsp       ; Set rsi to receive buffer (reuse stack space)

    xor rdx, rdx       ; Clear rdx register
    mov dx, 0x104      ; Set rdx to the size of the buffer

    syscall            ; Perform syscall to read the response

    ; Write response to the console
    xor rax, rax       ; Clear rax register
    mov al, 0x1        ; Syscall number for write in x64

    xor rdi, rdi       ; Clear rdi register
    mov dil, 0x1       ; Set rdi to stdout file descriptor

    mov rsi, rsp       ; Set rsi to point to the buffer with response

    xor rdx, rdx       ; Clear rdx register
    mov dl, 0x30       ; Set rdx to the number of bytes to write

    syscall            ; Perform syscall to write the response to the console
