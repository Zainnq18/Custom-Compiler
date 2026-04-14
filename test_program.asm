; ====== Generated Assembly-like Target Code ======

SECTION .data
    str_1  db  "Enter a number: ", 0
    str_2  db  "Factorial = ", 0

SECTION .text
    GLOBAL main


program_factorial:

func_computeFact:
    MOV AX, x
    CMP AX, 1
    JLE _cmp_true_9
    MOV t1, 0
    JMP _cmp_end_9
_cmp_true_9:
    MOV t1, 1
_cmp_end_9:
    MOV AX, t1
    CMP AX, 0
    JE  L1
    MOV AX, 1
    MOV f, AX
    JMP L2

L1:
    MOV AX, x
    SUB AX, 1
    MOV t2, AX
    PUSH t2
    CALL computeFact
    ADD SP, 2
    MOV t3, AX
    MOV AX, x
    IMUL AX, t3
    MOV t4, AX
    MOV AX, t4
    MOV f, AX

L2:
    MOV AX, f
    MOV computeFact, AX
    MOV AX, computeFact
    RET

main:
    MOV AX, OFFSET str_1
    CALL write_str
    ; read integer -> n
    CALL read_int
    MOV n, AX
    PUSH n
    CALL computeFact
    ADD SP, 2
    MOV t5, AX
    MOV AX, t5
    MOV result, AX
    MOV AX, OFFSET str_2
    CALL write_str
    MOV AX, result
    CALL write_int
    RET