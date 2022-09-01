;Boolean Logic pdf-5
;for 2 bits increment 

.include "/home/chirag/assembly/defs/m328Pdef.inc"

ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output


ldi r16,0b00000001 ;x
ldi r17,0b00000000 ;y
eor r16,r17         ; x xor y b
ldi r20,0b00000001
eor r17,r20          ;y^
ldi r20, 0b00000010	;counter = 2

	
lsl r16
or r16 , r17   
rcall loopw            	;calling the loopw routine

out PORTD,r16		    ;writing output to pins 2,3,4,5


Start:
rjmp Start

;loop for bit shifting
loopw:	lsl r16			;left shift
	dec r20			    ;counter --
	brne	loopw	    ;if counter != 0
	ret
