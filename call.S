print_abom:
    mov $1, %rax
    mov %rdi, %rsi
    mov $1, %rdi
    mov $24, %rdx
    syscall
    ret
