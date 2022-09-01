//Takes a number as input and prints the next number as output            // uses all 3 IC

#include <avr/io.h>

#include <util/delay.h>

#include <stdbool.h>




int main (void)

{

 bool A,B,C,D;                //output 

 bool a=0,b=0,c=0,d=0;

 DDRD = 0b00111100;           //pin 2,3,4,5 enabled   6,7 inputs

 DDRB = 0b00100000;          //pin 13 enabled

 PORTD = 0b11000000;        //reading from pins ;enabling pullup for 6,7
 
 DDRB  = 0b11111100;        //pin 8,9 inputs
 PORTB = 0b00000011;       //enabling pullups for 8,9


        while(1){




  PORTB = ((1 <<  PB5));

  _delay_ms (200L);

  D=(!d);

  C=((c&&(!d))||((!a)&&(!c)&&(d)));

  B=((b && (!d)) || (b && (!c)) || ((!b) && c && d));

  A=((a && (!d)) || (b && c && d));

                PORTD |= (D << 2);     //pin 2 will assign whatever D value has

                PORTD |= (C << 3);

                PORTD |= (B << 4);

                PORTD |= (A << 5);

                d = (PIND & (1 << PIND6)) == (1 << PIND6);   

                c = (PIND & (1 << PIND7)) == (1 << PIND7);

                b = (PINB & (1 << PINB0)) == (1 << PINB0);

                a = (PINB & (1 << PINB1)) == (1 << PINB1);

  PORTB = ((0 <<  PB5));

   _delay_ms (200L);

 }

        return 0;

}
