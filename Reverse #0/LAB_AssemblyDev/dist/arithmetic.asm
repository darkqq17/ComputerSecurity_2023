mov eax, dword [rsp]
imul edx, eax, 9
add edx, 7

mov ebx, dword [rsp]
mov ecx, dword [rsp+4]
add eax, ecx
sub ebx, ecx

mov ecx, dword [rsp+8]
neg ecx
