;hello
;using assembly language for turning LED on


.include "/home/chirag/assembly/defs/m328Pdef.inc"


  ldi r16,0b01000000
  out DDRB,r16
  ldi r17,0b01000000
  out PortB,r17
Start:
  rjmp Start
