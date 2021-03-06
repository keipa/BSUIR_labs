; ------------------------------------------------------------
; Определения структур данных и констант
; ------------------------------------------------------------

STRUC   desc_struc      ; структура дескриптора
        limit   dw      0       ; предел
        base_l  dw      0       ; мл. слово физического адреса
        base_h  db      0       ; ст. байт физического адреса
        access  db      0       ; байт доступа
        rsrv            dw      0       ; зарезервировано
ENDS            desc_struc

STRUC   idt_struc               ; вентиль прерывания
        destoff dw      0       ; смещение обработчика
        destsel dw      0       ; селектор обработчика
        nparams db      0       ; кол-во параметров
        assess  db       0       ; байт доступа
        rsrv       dw     0       ; зарезервировано
ENDS            idt_struc

STRUC   idtr_struc              ; регистр IDTR
        idt_lim dw      0       ; предел IDT
        idt_l   dw      0       ; мл. слово физического адреса
        idt_h   db      0       ; ст. байт физического адреса
        rsrv            db      0       ; зарезервировано
ENDS            idtr_struc

; ---------------------------------------------------------------
; Биты байта доступа

ACC_PRESENT     EQU     10000000b ; сегмент есть в памяти
ACC_CSEG                EQU     00011000b ; сегмент кода
ACC_DSEG                EQU     00010000b ; сегмент данных
ACC_EXPDOWN     EQU     00000100b ; сегмент расширяется вниз
ACC_CONFORM     EQU     00000100b ; согласованный сегмент
ACC_DATAWR      EQU     00000010b ; разрешена запись
ACC_INT_GATE    EQU     00000110b ; вентиль прерывания
ACC_TRAP_GATE   EQU     00000111b ; вентиль исключения

; ------------------------------------------------------------
; Типы сегментов

; сегмент данных

DATA_ACC = ACC_PRESENT OR ACC_DSEG OR ACC_DATAWR

; сегмент кода

CODE_ACC = ACC_PRESENT OR ACC_CSEG OR ACC_CONFORM

; сегмент стека

STACK_ACC = ACC_PRESENT OR ACC_DSEG OR ACC_DATAWR OR ACC_EXPDOWN

; байт доступа сегмента таблицы IDT

IDT_ACC         =       DATA_ACC

; байт доступа вентиля прерывания

INT_ACC         =       ACC_PRESENT OR ACC_INT_GATE

; байт доступа вентиля исключения

TRAP_ACC        =       ACC_PRESENT OR ACC_TRAP_GATE

; ------------------------------------------------------------
; Константы

STACK_SIZE      EQU     0400    ; размер стека
B_DATA_SIZE     EQU     0300    ; размер области данных BIOS
B_DATA_ADDR     EQU     0400    ; адрес области данных BIOS
MONO_SEG                EQU     0b000   ; сегмент видеопамяти
                                                ;  монохромного видеоадаптера
COLOR_SEG               EQU     0b800   ; сегмент видеопамяти
                                                ; цветного видеоадаптера
CRT_SIZE                EQU     4000    ; размер сегмента видеопамяти
                                        ;  цветного видеоадаптера
MONO_SIZE               EQU     1000    ; размер сегмента видеопамяти
                                        ;  монохромного видеоадаптера

CRT_LOW         EQU     8000    ; мл. байт физического адреса
                                        ;  сегмента видеопамяти
                                        ;  цветного видеоадаптера
MONO_LOW                EQU     0000    ; мл. байт физического адреса
                                        ;  сегмента видеопамяти
                                        ;  монохромного видеоадаптера

CRT_SEG         EQU     0Bh     ; ст. байт физического адреса
                                        ;  сегмента видеопамяти
CMOS_PORT               EQU     70h     ; порт для доступа к CMOS-памяти
PORT_6845               EQU     0063h   ; адрес области данных BIOS,
                                                ; где записано значение адреса
                                                ; порта контроллера 6845
COLOR_PORT      EQU     03d4h   ; порт цветного видеоконтроллера
MONO_PORT               EQU     03b4h   ; порт монохромного видеоконтроллера
STATUS_PORT     EQU     64h             ; порт состояния клавиатуры
SHUT_DOWN               EQU     0feh            ; команда сброса процессора
VIRTUAL_MODE    EQU     0001h   ; бит перехода в защищённый режим
A20_PORT                EQU     0d1h    ; команда управления линией A20
A20_ON          EQU     0dfh    ; открыть A20
A20_OFF         EQU     0ddh    ; закрыть A20
KBD_PORT_A      EQU     60h     ; адреса клавиатурных
KBD_PORT_B      EQU     61h     ;   портов
INT_MASK_PORT   EQU     21h     ; порт для маскирования прерываний
EOI                     EQU     20      ; команда конца прерывания
MASTER8259A     EQU     20      ; первый контроллер прерываний
SLAVE8259A      EQU     0a0     ; второй контроллер прерываний

; ------------------------------------------------------------
; Селекторы, определённые в таблице GDT

DS_DESCR                =       (gdt_ds - gdt_0)
CS_DESCR                =       (gdt_cs - gdt_0)
SS_DESCR                =       (gdt_ss - gdt_0)
BIOS_DESCR      =       (gdt_bio - gdt_0)
CRT_DESCR               =       (gdt_crt - gdt_0)
MDA_DESCR               =       (gdt_mda - gdt_0)

; ------------------------------------------------------------
; Маски и инверсные маски для клавиш

L_SHIFT         equ     0000000000000001b
NL_SHIFT                equ     1111111111111110b

R_SHIFT         equ     0000000000000010b
NR_SHIFT                equ     1111111111111101b

L_CTRL          equ     0000000000000100b
NL_CTRL         equ     1111111111111011b

R_CTRL          equ     0000000000001000b
NR_CTRL         equ     1111111111110111b

L_ALT           equ     0000000000010000b
NL_ALT          equ     1111111111101111b

R_ALT           equ     0000000000100000b
NR_ALT          equ     1111111111011111b

CAPS_LOCK               equ     0000000001000000b
SCR_LOCK                equ     0000000010000000b

NUM_LOCK                equ     0000000100000000b
INSERT          equ     0000001000000000b
