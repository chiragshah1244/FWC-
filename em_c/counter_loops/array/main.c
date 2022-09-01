//using an array for decade counter                                      //using only seven segment display only

#include <avr/io.h>
#include <util/delay.h>
#include "sevenseg.h"
 
void sevenseg(int);
int main (void)
{

//defining integer array p	
 const int p[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
 int i;
  //set PD2-PD7 as output pins 0xFC=0b11111100 (binary)
  DDRD   |= 0xFC;                                                         //enabling pin 2,3,4,5,6,7 for output.  same as pinMode in IDE
  //set 0 as output pin in portB of 0th pin                             
  DDRB   |= ((1 << DDB0));                                                //i.e pin no 8
 
  while (1)                                                               // INFINITE LOOP 
  {
	//loop counting from 0 to 9
  for (i=0; i < 10; i++)
	{

		sevenseg(p[i]);
		_delay_ms (1000L);		
	}
	}
  /* . */
  return 0;

}
