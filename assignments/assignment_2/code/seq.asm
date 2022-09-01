.include "/home/chirag/assembly/defs/m328Pdef.inc"

.def temp=r28
.def result=r29
.def d2=r30
.def d1=r31
.def d0=r1
.def y=r2

;for clock
ldi r16, high(RAMEND) 
out SPH, r16
ldi r16, low(RAMEND)
out SPL, r16

;output and input Pins
ldi r16, 0b00111100 ;identifying output pins 2,3,4,5(1's) and input pins 6,7(0's)
out DDRD,r16		;declaring pins as output and input
ldi r18, 0b00111100 ;identifying input pins 8,9 . 
out DDRB,r18        

ldi r16, 0b00000101 ;clk
out TCCR0B, r16

loopw:
in r17,PIND

mov r20,r17
ldi r19 ,0b01000000  ;interested on pin 6
and r20,r19  ;r20-q2         pin-6
lsr r20      ;shift  
lsr r20 
lsr r20 
lsr r20 
lsr r20 
lsr r20 

mov r24,r20     
ldi r16,0x01
eor r24,r16  ;q2'  

mov r21,r17
ldi r19,0b10000000
and r21,r19            ; r21-q1       pin-7
lsr r21 
lsr r21 
lsr r21 
lsr r21 
lsr r21 
lsr r21 
lsr r21 

mov r25,r21 
ldi r16,0x01
eor r25,r16  ;q1'
	
in r17,PINB  ;reading i/p values from pinb 

mov r22,r17 
ldi r19,0b00000001
and r22,r19            ; r22-q0       pin-8

mov r26, r22 
ldi r16,0x01
eor r26,r16

mov r23,r17 
ldi r19,0b00000010
and r23,r19            ; r23-x        pin-9
lsr r23

mov r27,r23    ;x' 
ldi r16,0x01
eor r27,r16

;got values for q2,q1,q0 and x 
;operation for d2
mov temp,r25 ; q1'--> temp 
and temp,r23 ; (q1'and x)--->temp
mov result,temp

mov temp,r24 ; q2'--> temp
and temp,r22 ;(q2'and q0)-->temp
and temp,r23 ;(q2'and q0 and x)--->temp
or result,temp

mov d2,result

;operation for d1
mov temp,r24 ;q2'-->temp
and temp,r21 ;(q2'and q1)-->temp
and temp,r26 ; (q2'and q1 and q0')-->temp
mov result,temp

mov temp,r24 ;q2'-->temp
and temp,r25 ;(q2' and q1') -->temp
and temp,r22 ;(q2' and q1' and q0) -->temp
and temp,r27 ;(q2' and q1' and q0 and x') -->temp
or result,temp

mov d1,result

;operation for d0
mov temp,r25 ;q1'-->temp
and temp,r26 ;(q1'and q0')-->temp
mov result,temp

mov temp,r25 ;q1'-->temp
and temp,r23 ;(q1' and x)-->temp
or result,temp

mov temp,r20 ;q2-->temp
and temp,r25 ;(q2 and q1')-->temp
or result,temp

mov temp,r24 ;q2'-->temp
and temp,r26 
and temp,r23
or result,temp

mov temp,r24
and temp,r21
and temp,r22
and temp,r27
or result,temp

mov d0,result

;operation for y
mov temp,r20
and temp,r26
and temp,r27
mov result,temp

mov temp,r20
and temp,r22
and temp,r23
or result,temp

mov y,result
;for q2
lsl d2
lsl d2
;for q1
lsl d1
lsl d1
lsl d1
;for q0
lsl d0
lsl d0
lsl d0
lsl d0
;for x
lsl y
lsl y
lsl y
lsl y
lsl y

or d2,d1
or d2,d0
or d2,y
out PORTD,d2  ;output pins

;for clk
sbi PORTB,5
rcall DELAY
cbi PORTB,5
rcall DELAY

rjmp loopw


DELAY:
ldi r19, 0x50 

DELAY_loop:
in r16, TIFR0
andi r16, 0x01  ; Check if timer overflow (given 0x02 which mask for compare)
breq DELAY_loop ; If not, keep checking
ldi r16, 0x01   ; Clear flag to check again
out TIFR0, r16
dec r19
brne DELAY_loop
ret
