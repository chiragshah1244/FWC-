//Blink LEDthrough an assembly routine

#include <avr/io.h>

//Function declared in initasm.S
extern void init(void);
//Function declared in displedasm.S
extern void disp_led(uint8_t);
//Function declared in delayasm.S
extern void delay(uint8_t, uint8_t, uint8_t);

 int main (void)
{
  while (1) {
	  init();                                                             //enables pin 13 as output
	//turn led off    	  
	  disp_led(0);                                                        //input to led as LOW
	delay(0, 0, 54);                                                      //delay	  
	//turn led on
	  disp_led(1);                                                         //input to led as High
	delay(0, 0, 54);	  	                                               //delay
  } 
  return 0;
}
