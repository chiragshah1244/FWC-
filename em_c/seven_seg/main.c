//Prints a decimal number on the display

#include <avr/io.h>
 
int main (void)
{
	
	
 //set PD2-PD7 as output pins 0xFC=0b11111100 (binary)
  DDRD   |= 0xFC;             //  enabling pin 2,3,4,5,6,7 for output.  same as pinMode in IDE
  //set PB0 as output pin
  DDRB    |= ((1 << DDB0));   //enabling pin 8 for output.                
 
  while (1)  ; //Infinite loop i.e always true.
  {
//turn PB0 off
    PORTB = ((0 << PB0));    // setting pin 8 as high   / same as -digitalWrite(8,HIGH)
//turn PD2-PD7 on    
    PORTD = 0b10010000; 
  }
  /* . */
  return 0;

}

// DDRD-Data Direction Register of port D - for enabling input pins. (DDRs are all registers)
//DDB0 - IT WILL JUST ENABLE the 0th pin of port B.
