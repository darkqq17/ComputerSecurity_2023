add rax, 0x87
sub rbx, 0x63

xchg rcx, rdx

; Modify memory value 
add dword [rsp], 0xdeadbeef
sub dword [rsp+4], 0xfaceb00c

; Swap MEM[RSP+0x8:RSP+0xc] and MEM[RSP+0xc:RSP+0x10]
mov edi, dword [rsp+8]    
mov esi, dword [rsp+0xc]
mov dword [rsp+8], esi  
mov dword [rsp+0xc], edi
