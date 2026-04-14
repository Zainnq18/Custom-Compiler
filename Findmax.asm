; ====== Generated Assembly-like Target Code ======

SECTION .data

SECTION .text
    GLOBAL main


program_findMax:

main:
    ; read integer -> a
    CALL read_int
    MOV a, AX
    ; read integer -> b
    CALL read_int
    MOV b, AX
    MOV AX, a
    CMP AX, b
    JG _cmp_true_15
    MOV t1, 0
    JMP _cmp_end_15
_cmp_true_15:
    MOV t1, 1
_cmp_end_15:
    MOV AX, t1
    CMP AX, 0
    JE  L1
    MOV AX, a
    CALL write_int
    JMP L2

L1:
    MOV AX, b
    CALL write_int

L2:
    RET