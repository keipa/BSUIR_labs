.MODEL small
.STACK 256h
.data
; тексты сообщений
fnd db "symbol found ",'$'
nochar db  "symbol not found",'$'
;строка для поиска
string db "search symbol in this string ",10,13,'$'
.code
ASSUME ds:@data,es:@data
main:
mov ax,@data
mov ds,ax
mov es,ax ;настройка ES на DS
mov ah,09h
lea dx,string
int 21h ;вывод сообщения string
mov al,'a' ;символ для поиска - "а"(кириллица)
cld ;сброс флага df
lea di,string ;загрузка в es:di смещения строки
mov cx,28 ;для префикса repne - длина строки
;поиск в строке (пока искомый символ и символ в строке не совпадут)
;выход при первом совпадении
repne scas string
je found ;если равны - переход на обработку,
failed: ;иначе - выполняем некоторые действия
;вывод сообщения о том, что символ не найден
mov ah,09h
lea dx,nochar
int 21h ;вывод сообщения nochar
jmp exit ;на выход
found: ;совпали
mov ah,09h
lea dx,fnd
int 21h ;вывод сообщения fnd
;теперь, чтобы узнать место, где совпал элемент в строке,
;необходимо уменьшить значение в регистре di и вставить нужный обработчик
; dec di
;... вставьте обработчик
exit: ;выход
mov ax,4c00h
int 21h
end main
