.model   small
.stack   200h
.data
	AXPROC dw 200
	STRING_ONE DB ' INPUT 1-ST NUMBER: $'	
	STRING_TWO DB ' INPUT 2-ND NUMBER: $'
	STRING_RES DB ' RESULT: $'
	STRING_ESC DB 10, 13,'AGAIN:' , '$'
	STRING_BSP DB 10, 13, '$'
	MINUS DB '-','$'
	INONE DW 0
	INTWO DW 0
	TEN DW 10
	MCHEK DW 0
.code
start:
	MOV AX, @DATA	;WHAT IT IS??
	MOV DS, AX

	

	LEA DX,STRING_ONE
	MOV AH,09H	;STRING OUT
	INT 21H
	
	CALL INPROC
	MOV INONE,AX		;ONE IN
	
		

	LEA DX,STRING_TWO
	MOV AH,09H	;STRING OUT
	INT 21H

	CALL INPROC
	MOV INTWO,AX		;TWO IN	
	
		

	LEA DX,STRING_RES
	MOV AH,09H	;STRING OUT
	INT 21H

	
	XOR AX, AX
	
	XOR CX, CX
	XOR DX, DX

	;CALL COMPUTE
	
	MOV AX, INONE
	MOV CX, INTWO
	DIV CX

	;mov ax,10
	CALL OUTPROC	;OUTPUT  


MOV AH,4CH
INT 21H

OUTPROC PROC
	PUSH CX		;SAVE REGISTERS
	PUSH DX
	PUSH BX
	PUSH AX

        MOV BX, TEN	;PREPARE DECREASE CAPACITY
        XOR CX,CX	;COUNTER ZERO
        FOR1:
            XOR DX, DX 	;DX SHOULD BE ZERO
            DIV BX	;DECREASE CAPACITY
            PUSH DX	;RESIDUE GOING TO STACK
            INC CX	;INCREASE COUNTER FOR LOOP
            TEST AX,AX	;IF THE NUMBER BECOME NOT-ZERO START TO OUTPUT
            JNZ FOR1

        MOV AH, 02h	;OUTPUT FUNTCTION OF 21 BREAKING
        FOR2:
            POP DX	;TAKE DIGIT FROM THE STACK (1->5->6)
            ADD DL, 30H	;CONVERT TO THE CHARACHTERS
            INT 21h	;BREAKING
            LOOP FOR2	

	POP AX		;RESTORE REGISTERS
	POP BX
	POP DX
	POP CX

		
RET
OUTPROC ENDP


INPROC PROC

	PUSH BX		;SAVE ALL REGISTERS
	PUSH CX
	PUSH DX
	PUSH DI		;MAGIC REGISTER DI MUST BE SAVED
	XOR DI,DI 	;AND SHOULD BE NULL
	

STARTIN:
	
	XOR DX, DX
	XOR AX, AX
	
	MOV AH,08H	;EXACTLY INPUT TO THE AX REGISTER
	INT 21H

	XOR AH,AH
	CMP AL,13 	;AL STORE LAST SYMBOL. 13 - IS FOR ENTER
	JZ SAVING	;IF ENTER PRESSED STARTING SAVING TO THE REGISTER
	CMP AL,8 	;AL STORE LAST SYMBOL. 8 - IS FOR BACKSPACE
	JZ DELETE	;IF BACKSPACE PRESSED DELETING LAST SYMBOL
	CMP AL,27 	;AL STORE LAST SYMBOL. 27 - IS FOR ESCAPE
	JZ DELALL	;IF ESCAPE PRESSED DELETING ALL NUMBER

	CMP AL, '-'	;AL STORE LAST SYMBOL.
	JZ ADDMIN	;IF MINUS PRESSED. MINUS ADDED

			;NOT-TO-INPUT STRING CHECKING
	CMP AL, '9'
	JA STARTIN	;IF AL SYMBOL MORE THAN '9' STARTING TO ENTER SYMBOL AGAIN
	CMP AL, '0'
	JB STARTIN	;IF AL SYMBOL LESS THAN '0' STARTING TO ENTER SYMBOL AGAIN

	
	MOV AH,02H 	;OUTPUT CHECKED SYMBOL
	MOV DL,AL	;DL STORE SYMBOL TO OUTPUT
	INT 21H

	XOR AH,AH
	SUB AX, 30H	;CONVERT SYMBOL TO THE DIGIT
	PUSH AX		;SAVE DIGIT

	MOV AX, DI	;MOVE LAST VALUE TO AX REGISTER TO PREPARE CHECKING
	MOV BX, TEN	;CHECKING TO THE OVERLIMIT
	MUL BX		;MULTIPLY
	JC DELALL	;IF OVERLIMIT GOTO ESCAPE
	
	POP DI
	ADD AX, DI	;SUM A HOLE NUMBER(AX) * 10 + CURRENT DIGIT(DI)
	CMP AX,32766
	JNC DELALL
	
	MOV DI,AX	;SAVING NUMBER
	JMP STARTIN	;ADDING NEW DIGIT


DELALL:
	XOR AX,AX	;CLEAR AX REGISTER
	XOR DI,DI	;CLEAR DI(SAVED NUMBER) REGISTER
	MOV MCHEK, 0
	LEA DX,STRING_ESC
	MOV AH,09H	;STRING OUT
	INT 21H
	
	;CALL INPROC
	JMP STARTIN	;START INPUT AGAIN

ADDMIN:
	CMP DI, 0	;INPUT MINUS AT BEGINNING ONLY
	JNZ STARTIN
	PUSH CX
	MOV CX, MCHEK
	CMP CX,0
	JNZ STARTIN
	POP CX
	LEA DX, MINUS	;"-" CHARACHTER
	MOV AH,09H	;STRING OUT
	INT 21H		;BREAKING

	PUSH CX
	MOV CX, MCHEK
	INC CX
	MOV MCHEK, CX
	POP CX
	JMP STARTIN
	

DELETE:

;BACKSPACE
	
	LEA DX,STRING_BSP
	MOV AH,09H	;STRING OUT
	INT 21H
	XOR DX, DX
	MOV AX, DI
	MOV BX, TEN
	DIV BX
	
	CALL OUTPROC
	MOV DI, AX
	XOR DX,DX
	
	JMP STARTIN
SAVING:
	LEA DX,STRING_BSP
	MOV AH,09H	;STRING OUT
	INT 21H

	MOV AX,DI	;MOVEING NUMBER TO AX REGISTER
	MOV MCHEK,0
	POP DI		;RESTORE REGISTERS
	POP DX
	POP CX
	POP BX
RET
INPROC ENDP



COMPUTE PROC

MOV AX, INONE		;INONE/INTWO
DIV INTWO


;DIV TWO DIGITS

RET
COMPUTE ENDP



END START