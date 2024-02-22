mov eax, [rsp] ; load a into EAX
mov ebx, [rsp+4] ; load b into EBX
mov ecx, [rsp+8] ; load c into ECX
mov edx, [rsp+0xc] ; load d into EDX

; Compare a and b, store maximum in EAX
cmp eax, ebx
jge skip
mov eax, ebx
skip:

; Compare c and d, store minimum in EBX (unsigned)
mov ebx, edx
cmp ecx, edx
jae skip2
mov ebx, ecx
skip2:

; Check c is even or odd
test ecx, 1 ; Test the least significant bit of c
jz even

; If c is odd
sar ecx, 3
jmp done

; If c is even
even:
shl ecx, 2

done:
