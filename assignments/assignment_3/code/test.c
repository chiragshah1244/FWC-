#include <avr/io.h>
#include <util/delay.h>

#define CLK_BIT 5

int q0, q1, q2, x, d0, d1, d2,y;

void gpio_init(void){
	
 DDRD = 0b00111100;            //pin 2,3,4,5 enabled as output pins(1's) //pin 6,7 as input pins(0's)

 DDRB = 0b00100000;           //pin 13 enabled as output(1)

 //DDRD = 0b00111111 ;          //6,7 inputs
 //PORTD = 0b11000000;        //reading from pins ;enabling pullup for 6,7
 
 
 DDRB  = 0b11111100;         //pin 8,9 inputs
// PORTB = 0b00000011;         //enabling pullups for 8,9
	
}

void fsm_read(void){
  uint8_t input = PIND;      //digital read 
  if((input & 0x40)==0)
  q2=0;
  else q2=1;
  if((input & 0x80)==0)
  q1=0;
  else q1=1;
  
  input=PINB;
  if((input & 0x01)==0)
  q0=0;
  else q0=1;
  if((input & 0x02)==0)
  x=0;
  else x=1;
}

void fsm_update(void){
  uint8_t output;

  d2=(!q1 && x) || (!q2 && q0 && x);
  d1=((!q2 && q1 && !q0) || (!q2 && !q1 && q0 && !x));
  d0=(!q1 && !q0) || (!q1 && x) || (q2 && !q1) || (!q2 && !q0 && x) || (!q2 && q1 && q0 && !x);
  y=(q2 && !q0 && !x) || (q2 && q0 && x);

  output = (d2<<2) | (d1<<3) | (d0<<4) | (y<<5);
  PORTD = output;
  
}

void clock_pulse(void){
	PORTB |= (1<<CLK_BIT);
  _delay_ms(2000);
  PORTB &= ~(1<<CLK_BIT);
  _delay_ms(2000);
  
}

int main (void)
{
	gpio_init();
  while(1){
    fsm_read();
    fsm_update();
    clock_pulse();
  }
  return 0;
}
