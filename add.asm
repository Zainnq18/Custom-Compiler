; ====== Generated Assembly-like Target Code ======

SECTION .data
    str_1  db  "Enter first number: ", 0
    str_2  db  "Enter second number: ", 0
    str_3  db  "Sum = ", 0

SECTION .text
    GLOBAL main


program_addNumbers:

main:
    MOV AX, OFFSET str_1
    CALL write_str
    ; read integer -> a
    CALL read_int
    MOV a, AX
    MOV AX, OFFSET str_2
    CALL write_str
    ; read integer -> b
    CALL read_int
    MOV b, AX
    MOV AX, a
    ADD AX, b
    MOV t1, AX
    MOV AX, t1
    MOV sum, AX
    MOV AX, OFFSET str_3
    CALL write_str
    MOV AX, sum
    CALL write_int
    RET