.include "/home/chirag/assembly/defs/m328Pdef.inc"

	ldi r16, 0b00111100 ;identifying output pins 2,3,4,5
	;asign full 7bit b value in r16 
	out DDRD,r16		;declaring pins as output
	;it  enables pins which are 1 
	ldi r16,0b00000100	;loading the number 2 in binary  //giving INPUT here  
	;asigns full 7bit b value in r16
	out PORTD,r16		;writing output to pins 2,3,4,5
	;port d has 0-7 pins so above b value will compair with 1th b value i.e only 2345 pins will assign 0001
	
Start:
	rjmp Start
	
;for abcd we are giving as inputs.


;giving INPUTS in r16 as abcd=2345
;
