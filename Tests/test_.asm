section .data
HelloVar_pri db "Hello"
HelloVar_pri_LEN equ $ - HelloVar_pri

section .text
global _start

_start:
mov ecx, HelloVar_pri
mov edx, HelloVar_pri_LEN
call print
call cleanup32
mov ebx, 0
call return

print:
mov eax, 4
mov ebx, 1
int 80h

input:
mov eax, 3
mov ebx, 1
int 80h

return:
mov eax, 1
int 80h

cleanup32:
xor eax, eax
xor ebx, ebx
xor ecx, ecx
xor edx, edx
xor esi, esi
xor ebp, ebp
ret

