// params: char* msg, int len
print_abom:
    mov $1, %rax
    mov %rsi, %rdx
    mov %rdi, %rsi
    mov $1, %rdi
    syscall
    ret
