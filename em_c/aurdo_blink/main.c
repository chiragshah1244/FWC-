//Turns LED on and off

#include <avr/io.h>
#include <util/delay.h>

 
int main (void)
{
	
  /* Arduino boards have a LED at PB5 */
  //set PB5, pin 13 of arduino as output
  DDRB    |= ((1 << DDB5));
  
  while (1) {
//turn led off    
    PORTB = ((0 <<  PB5));  //giving 5th pin as low ; digitalWrite(13,LOW)
	_delay_ms(500);
//turn led on
    PORTB = ((1 <<  PB5));  //giving 5th pin as HIGH ; digitalWrite(13,HIGH)
    _delay_ms(100);
}


  /* . */
  return 0;

}
