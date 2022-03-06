bits 64

; add rsp, 40
lea rbp, [rsp+40]
mov [rsp], rbp
ret
