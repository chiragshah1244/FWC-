

;7447 decoder i/o


.include "/home/chirag/assembly/defs/m328Pdef.inc"

	ldi r17, 0b11000011 ; identifying input pins 10,11,12,13   for inputs its 0 for OUTPUTS itys 1 
	out DDRB,r17		; declaring pins as input
	ldi r17, 0b11111111 ; //pullups for INPUTS
	out PORTB,r17		; activating internal pullup for pins 10,11,12,13  
	in r17,PINB
	
	ldi r16, 0b00111100 ;identifying output pins 2,3,4,5 is abcd of IC 
	out DDRD,r16		;declaring pins as output
	out PORTD,r17		;writing output to pins 2,3,4,5
	
Start:
	rjmp Start

;FOR digitalWrite OR digitalRead we use PORT_ .
;For pinMode we use DDR_.


;giving inputs manually {+5V and ground}
