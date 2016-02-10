model small
.stack 100h
.386
.data
           STRING_A DB ' INPUT A: $'
           STRING_B DB ' INPUT B: $'
           STRING_C DB ' INPUT C: $'
           STRING_X1 DB ' X1 : $'
           STRING_X2 DB ' X2 : $'
           STRING_ENT DB 10, 13, '$'
           STRING_D db 10,13, ' D  = $'
           STRING_CONT db 10,13, ' Continue y/n?    $'
           STRING_NOTKVADR db 10,13, ' Format error. Enter correct format     $'
                                                                                                                                                            ;������� ���������� ������������� Ax^2+Bx+C
            a dd ?                                                                                                                                          ;����������� ��� X^2
            b dd ?                                                                                                                                          ;����������� ��� X
            nb dd ?                                                                                                                                         ;(-b)
            c dd ?                                                                                                                                          ;��������� ����
            d dd ?                                                                                                                                          ;�������� �������������
            two dd 2.0                                                                                                                                 ;���
            four dd 4.0                                                                                                                                ;������
            kd dd ?                                                                                                                                    ;������ �� �������������
            nkd dd ?                                                                                                                                   ;negative ������ �� �������������
            x1 dd ?                                                                                                                                    ;������ 1
            x2 dd ?                                                                                                                                    ;������ 2

.code
        start:
        mov ax, @data                                                                                                      ;������� ������� � �������
        mov ds, ax                                                                                                         ;� ������� ���� DS

        restart:

        lea dx,STRING_ENT                                                                                                      ;�������
        mov ah,09h	                                                                                                       ;�� �����
        int 21h
                                                                                                                                ;����� �������� � ������ �������������� �������������

        lea dx,STRING_A                                                                                                         ;�����
        mov ah,09h	                                                                                                        ;���������
        int 21h                                                                                                                 ;INPUT A
        call infloat                                                                                                            ;����� ������� ����� ������������� �����
        fstp a                                                                                                                  ;�������� � �������� ����� st() �������� � ������� ��� � ����������
        cmp a,0
        jne zero

        lea dx,STRING_NOTKVADR                                                                                                      ;�������
        mov ah,09h	                                                                                                         ;�� �����
        int 21h
        je restart
        zero:
        lea dx,STRING_B                                                                                                       ;�����
        mov ah,09h	                                                                                                      ;���������
        int 21h                                                                                                               ;INPUT B
        call infloat                                                                                                          ;����� ������� ����� ������������� �����
        fstp b                                                                                                                ;�������� � �������� ����� st() �������� � ������� ��� � ����������

        lea dx,STRING_C                                                                                                            ;�����
        mov ah,09h	                                                                                                           ;���������
        int 21h                                                                                                                    ;INPUT C
        call infloat                                                                                                               ;����� ������� ����� ������������� �����
        fstp c                                                                                                                     ;�������� � �������� ����� st() �������� � ������� ��� � ����������

        fstp st(0)                                                                                                                ;�������
        fstp st(1)                                                                                                                ;�����
        fstp st(2)                                                                                                                ;st()

        fld b                                                                                                                       ; s(0)=b
        fmul b                                                                                                                      ;s(0)=b*b
        fld a                                                                                                                       ; s(0) = a, s(1)=b*b
        fmul c                                                                                                                      ;s(0) = a*c, s(1)=b*b
        fmul four                                                                                                                   ;s(0) =4*a*c, s(1)=b*b
        fsub                                                                                                                        ;s(0) = b*b-4*a*c
        fstp d
        fld d
        lea dx,STRING_D                                                                                                          ;�����
        mov ah,09h	                                                                                                         ;���������
        int 21h                                                                                                                  ;D
        call outfloat

        lea dx,STRING_ENT                                                                                                     ;�������
        mov ah,09h	                                                                                                      ;�� �����
        int 21h                                                                                                               ;������
        fld d
                                                                                                                                ;�������� �� ������������� ������������
          ftst                                                                                                                  ;���������� ���������� � ����
          fstsw ax                                                                                                              ;��������� �����
          sahf                                                                                                                  ; �������� �������� �������� ah � ������� ���� ��������� ��������. ����� ����� ���� ������������ ��������� ��������� ��������
          jc restart                                                                                                                ;���� ���� ��������, �� ��������� �� �����

          fsqrt                                                                                                                     ;s(0) =sqrt(b*b-4*a*c)
          fstp kd                                                                                                                   ;�������� ������ ���������� �������������

          fstp st(0)                                                                                                                  ;st(0)=0
          fldz                                                                                                                        ;st(0)=0, st(1)=0
          fld b                                                                                                                       ;st(0)=b, st(1)=0
          fsub                                                                                                                        ;st(0)=-b
          fstp nb                                                                                                                     ;������ �� ����� �������� � ��������� nb

          fstp st(0)                                                                                                                 ;st(0)=0
          fldz                                                                                                                       ;st(0)=0, st(1)=0
          fld kd                                                                                                                     ;st(0)=kd, st(1)=0
          fsub                                                                                                                       ;st(0)=-kd
          fstp nkd                                                                                                                   ;���������  nkd   (������ ���������,���� ���� �������� �� fchs)

          fld nb                                                                                                                       ;st(0)=nb
          fld nkd                                                                                                                      ;st(0)=nkd st(1)=nb
          fadd                                                                                                                         ;st(0) = nkd + nb
          fld a                                                                                                                        ;st(0)=a, st(1)=nkd+nb
          fmul two                                                                                                                     ;st(0)=2*a
          fdiv                                                                                                                         ;st(0)=(nkd+nb)/(2*a)
          lea dx,STRING_X1                                                                                                       ;�����
          mov ah,09h	                                                                                                         ;����������
          int 21h                                                                                                                ;���������
          call outfloat                                                                                                          ;����� ���������� ���������� X1

          lea dx,STRING_ENT                                                                                                      ;�������
          mov ah,09h	                                                                                                         ;�� �����
          int 21h                                                                                                                ;������
          fld nb                                                                                                                 ;st(0)=nb
          fld kd                                                                                                                 ;st(0)=nkd st(1)=nb
          fadd                                                                                                                   ;st(0) = nkd + nb
          fld a                                                                                                                  ; st(0)=a, st(1)=nkd+nb
          fmul two                                                                                                               ;st(0)=2*a
          fdiv                                                                                                                   ;st(0)=(kd+nb)/(2*a)
          lea dx,STRING_X2                                                                                                       ;�����
          mov ah,09h	                                                                                                         ;����������
          int 21h                                                                                                                ;���������
          call outfloat                                                                                                          ;����� ���������� ���������� X1

        lea dx,STRING_CONT                                                                                                         ;�����
                mov ah,09h	                                                                                                        ;���������
                int 21h                                                                                                                 ;INPUT A

          mov     ah, 01h                                                                                                    ; ������  ������
          int     21h
          cmp     al, 'y'                                                                                                         ;���������� �������� �������� � �������� "-"
          je     restart                                                                                                      ;���� "-" �� ����������, ���� ��� �� ���������

            mov ah, 4ch                                                                                                          ;������� � ah ��� ��������� ��� ������ �� ���������
            int 21h                                                                                                              ;�����������

            infloat proc    near
                push    ax                                                                                                       ;���������� �������� ax
                push    dx                                                                                                       ;�������� dx
                push    si                                                                                                       ;�������� si
                                                                                                                                 ;���������  ����, ����� ������� ������� � ��� �����-������ �����.
                push    bp                                                                                                       ;�������� bp
                mov     bp, sp                                                                                                   ;�������� � bp ��������� �����
                push    10                                                                                                       ;������� � ����  10
                push    0                                                                                                        ;������� � ����  0
                xor     si, si                                                                                                   ; � SI �������� ����.

                                                                                                                                 ; ������ ����������� �����. ������� ��� ����.
                fldz
                mov     ah, 01h                                                                                              ; ������ ������ ������
                int     21h                                                                                                  ;����� ������ ������� 21�� ����������
                cmp     al, '-'                                                                                              ;���������� �������� �������� � �������� "-"
                jne     short @if1                                                                                           ;���� "-" �� ����������, ���� ��� �� ��������� ��������� �������
                inc     si                                                                                                   ;����������� ����� � �������� si
        @if0:
                mov     ah, 01h                                                                                              ; ������  ������
                int     21h                                                                                                  ;����� ������ ������� 21�� ����������


        @if1:
                cmp     al, '.'                                                                                               ;���� ������� �����, ��
                je      short @if2                                                                                            ; ��������� ������� �����


                cmp     al, 39h                                                                                                       ;���������
                ja      short @if5                                                                                                    ;��� ������ �����,
                sub     al, 30h                                                                                                       ;� � ������ ���� �������� �� �����,
                jb      short @if5                                                                                                    ;�� ��������� �� ����� ����������� ����
                                                                                                                                      ;�������� � �� ��������� ������ � �������
                                                                                                                                      ; � �������� ���������� ������,
                mov     [bp - 4], al                                                                                                  ;���������� �������� ����� � ������
                fimul   word ptr [bp - 2]                                                                                             ;�������� ���� ����� �� 10
                fiadd   word ptr [bp - 4]                                                                                             ;������� � ���� ����� �������� �����
                jmp     short @if0                                                                                                    ;���������
        @if2:                                                                                                                         ;����� ���������� ������� �����
         fld1                                                                                                                         ; �������� � ���� ����� 1��
        @if3:
                mov     ah, 01h                                                                                                        ;���������
                int     21h                                                                                                            ;������

                cmp     al, 39h                                                                                                       ;���������
                ja      short @if4                                                                                                    ;��� ������ �����,
                sub     al, 30h                                                                                                       ;� � ������ ���� �������� �� �����,
                jb      short @if4                                                                                                    ; �� ��������� �� ����� ����������� ����

                mov     [bp - 4], al                                                                                          ; ����� ��������� � �� ��������� ������,
                fidiv   word ptr [bp - 2]                                                                                     ; �������� ��������� ������������� ������� �������,
                fld     st(0)                                                                                                 ;���������� � � ����
                fimul   word ptr [bp - 4]                                                                                     ; ��������� �� �������� �����, ��� ����� ������� � �� ������ �����
                faddp   st(2), st                                                                                             ; � ��������� �  ����������.
                jmp     short @if3                                                                                            ; ���������


        @if4:
        fstp    st(0)                                                                                                                 ;�� ������� ����� �������� �������� �����.
        @if5:
                mov     ah, 02h                                                                                                       ;����� �� �����
                mov     dl, 0Dh                                                                                                       ;������� �������
                int     21h
                test    si, si                                                                                                          ;���������  ������� �����
                jz      short @if6                                                                                                      ;���� ����  �� ����
                fchs                                                                                                                    ;�� ������ � ����� ����
        @if6:   leave
                pop     si                                                                                                              ;��������������� ������� si
                pop     dx                                                                                                              ;��������������� ������� dx
                pop     ax                                                                                                              ;��������������� ������� ax
                ret
        infloat endp



        outfloat proc near
                push    ax                                                                                                             ;��������� ������� ��
                push    cx                                                                                                             ;������� cx
                push    dx                                                                                                             ;������� dx
                push    bp                                                                                                             ;������� bp
                mov     bp, sp                                                                                                         ;�������� � bp ��������� �����
                push    10                                                                                                             ;������� � ����  10
                push    0                                                                                                              ;������� � ����  0

                ftst                                                                                                                   ; ��������� ����� �� ����, � ���� ��� �������������
                fstsw   ax                                                                                                             ;��������� �����
                sahf                                                                                                                   ;�������� �������� �������� ah � ������� ���� ��������� ��������.
                jnc   @of1                                                                                                             ;��������� ���������

                mov     ah, 02h                                                                                                        ;�������
                mov     dl, '-'                                                                                                        ;�����
                int     21h
                fchs                                                                                                                   ;���� ������ �����

        @of1:
                fld1
                fld     st(1)
                fprem                                                                                                                  ;������� �� ������� � ������� �����
                fsub    st(2), st                                                                                                      ; �������� �� ��������� �����
                fxch    st(2)                                                                                                          ;������ �������
                xor     cx, cx                                                                                                         ;������� cx ��� ����, ����� ������� ���������� ���� �� �������
                                                                                                                                       ; ������� ����� ����� �� ������,
        @of2:
                fidiv   word ptr [bp - 2]                                                                                              ;������� �� 10 �������
                fxch    st(1)                                                                                                          ;�������� ������� ������� � 1� �������
                fld     st(1)                                                                                                          ;�����  1    �����  �����

                fprem                                                                                                                  ;����� ���� ������� �� �������

                fsub    st(2), st                                                                                                      ;� �� ������������ ������� ��������� ������ ����� �����

                fimul   word ptr [bp - 2]               ;�������� ���� ������� �� 10
                fistp   word ptr [bp - 4]               ; �������� ����� �� ��������� ������ ������� �����.�� ����� ������� � ����� � ����� �������
                                                        ; ������ � ����� �������� � ������� 1 , 1-� ����� ����� ��� ������ ������� �������� ����� � �����, 2-� �����
                inc     cx                              ; �������� �������, ����� ����� ������� ������� ���� �� �����.
                push    word ptr [bp - 4]                                                                                            ; �����������
                fxch    st(1)                                                                                                        ;������ ������� ������� � ������ �������, ����� ������ ������ ����

                ftst                                                                                                                 ;����������� �� ����
                fstsw   ax                                                                                                           ;��������� �����
                sahf                                                                                                                 ;�������� ����
                jnz     short @of2                                                                                                   ; ��� ����� ���������, ���� �� ����� ����� �� ��������� ����.

                mov     ah, 02h                                                                                                 ;������� �����
        @of3:                                                                                                                   ;����� ��� ������ ��� ���� ����� �� ������� �� �����
                pop     dx                                                                                                      ; ����������� ��������� �����, ��������� � � ������ � �������.
                add     dl, 30h
                int     21h
                loop    @of3                                                                                                      ; � ���, ���� �� ������� ��� ����� �������� ���� cx
                                                                                                                                  ;������ � ������� ������
                fstp    st(0)
                fxch    st(1)                                                                                                       ;�������� �������
                ftst                                                                                                                ;�������� ������� ������� �����
                fstsw   ax
                sahf
                jz      short @of5                                                                                                  ; ���� � ��� �� ��� �� �����

                mov     ah, 02h
                mov     dl, '.'                                                                                                     ; ���� ��� ��-���� ���������, ������� �����
                int     21h
                mov     cx, 6                                                                                                       ;�������� 6���� ����� �������

        @of4:
                fimul   word ptr [bp - 2]                                                        ;�������� �������� ����� �� ������ (������� � ���, ��� �� �������� �� 10, � �� �����)
                fxch    st(1)                                                                    ;�� �� �������� ��� � � ������
                fld     st(1)                                                                    ;������ � ���� ����������� �� 10 �����

                fprem                                                                                                         ; ������� ����� �����
                fsub    st(2), st                                                                                             ; ������� �� ����������� �� 10����� ���� ������� �����
                fxch    st(2)                                                                                                 ;�������� ������� ���� � ������ �������

                fistp   word ptr [bp - 4]                                                         ; �������� ���������� ����� �� ��������� ������, ����� ����� ���� ����� � ��� ��������
                mov     ah, 02h                                                                   ; � ����� �������.
                mov     dl, [bp - 4]
                add     dl, 30h
                int     21h

                fxch    st(1)                                                                                               ;����� ��������� �� ������� ���� � �������
                ftst                                                                                                        ;(������������ ����� ������ ��� ����,
                fstsw   ax                                                                                                  ; ������ ��� ��� �������������� �������� ����� ����� ������������� )
                sahf
                loopnz  @of4                                                                                                ; ���� �� ������� 6 ���� (������� CX)

        @of5:
                fstp    st(0)                                                                                               ;������� ������� �����
                fstp    st(0)
                leave
                pop     dx                                                                                                  ;��������������� ��� ��������
                pop     cx
                pop     ax
                ret
        outfloat endp
        end start