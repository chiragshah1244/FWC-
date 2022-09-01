.include "/home/chirag/assembly/defs/m328Pdef.inc"
;OUTPUT
ldi r16, 0b00001100 ;identifying output pins 2,3,4,5
out DDRD,r16		;declaring pins as output

;INPUT
ldi r31,0b00111111;
out DDRD ,r16;

ldi r21, 0b11111111 ; //pullups for INPUTS
	out PORTD,r21		; activating internal pullup for pins 10,11,12,13  
	in r21,PINB
	
sbi DDRB, 5 ;set pin 13 as output pin (DDRB pin 5)
ldi r16, 0b00000101 ;the last 3 bits define the prescaler, 101 => division by 1024
out TCCR0B, r16 
;prescalar used = 1024. So new freq. of clock cycle = (16 MHz / 1024) = 16 kHz

clr r18 ;output bits. we are only interested in bit 6 from the right.

ldi r20,0b00100000	;initializing

loop:
	eor r18, r20 		;change the output of LED
	out PORTB, r18 
	ldi r19, 0b01000000 ;times to run the loop = 64 for 1 second delay
	rcall PAUSE 		;call the PAUSE label
	rjmp loop
	
PAUSE:	;this is delay (function)
lp2:	;loop runs 64 times
		IN r16, TIFR0 ;tifr is timer interupt flag (8 bit timer runs 256 times)
		ldi r17, 0b00000010
		AND r16, r17 ;need second bit
		BREQ PAUSE 
		OUT TIFR0, r17	;set tifr flag high
	dec r19
	brne lp2
	
	mov r22,r21
    ldi r23,0b00000001
    eor r22,r23
    mov r16,r22
    ldi r23,0b00000010
    mov r22,r21
    eor r22,r21
    mov r17,r22
    eor r16,r17         ; x xor y b
    ldi r23,0b00000001
    eor r17,r20          ;y^
    ldi r23, 0b00000010	;counter = 2

	
    lsl r16
    or r16 , r17   
    rcall loopw            	;calling the loopw routine

    out PORTD,r16		    ;writing output to pins 2,3,4,5
    ret

Start:
rjmp Start

;loop for bit shifting
loopw:	lsl r16			;left shift
	dec r23			    ;counter --
	brne	loopw	    ;if counter != 0
	ret
