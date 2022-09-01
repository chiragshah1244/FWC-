#include<Arduino.h>
void setup() 
{
    pinMode(2, OUTPUT);  //sets the dig pin 9 as OUTPUT
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);  
    pinMode(10,OUTPUT);          
}

void sevenseg (int a,int b,int c,int d,int e,int f,int g,int h)
{
  digitalWrite(2, a);  //Sets the dig pin 9 ON or OFF depending on the valve a.
  digitalWrite(3, b); 
  digitalWrite(4, c);
  digitalWrite(5, d); 
  digitalWrite(6, e); 
  digitalWrite(7, f);     
  digitalWrite(8, g); 
  digitalWrite(10,h);
}

void loop() 
{
sevenseg(0,0,0,0,0,0,1,0); //0
delay(500);
sevenseg(1,0,0,1,1,1,1,1);  //1
delay(500) ; 
sevenseg(0,0,1,0,0,1,0,0);  //2
delay(500);
sevenseg(0,0,0,0,1,1,0,0);  //3 
delay(500);
sevenseg(1,0,0,1,1,0,0,1);  //4 
delay(500);
sevenseg(0,1,0,0,1,0,0,1);  //5
delay(500);
sevenseg(0,1,0,0,0,0,0,1);  //6
delay(500);
sevenseg(0,0,0,1,1,1,1,1);  //7
delay(500);
sevenseg(0,0,0,0,0,0,0,0);  //8
delay(500);
sevenseg(0,0,0,0,1,0,0,1);  //9
delay(500);
sevenseg(1,1,1,1,1,1,0,1); //0
delay(500);
sevenseg(0,0,0,0,1,0,0,1);  //9
delay(500);
sevenseg(0,0,0,1,1,1,1,1);  //7
delay(500);
sevenseg(1,0,0,1,1,0,0,1);  //4 
delay(500);
sevenseg(0,0,0,0,0,0,1,0); //0
delay(500);
sevenseg(1,0,0,1,1,0,0,1);  //4 
delay(500);
sevenseg(0,0,0,1,1,1,1,1);  //7
delay(500);
sevenseg(0,1,0,0,1,0,0,1);  //5
delay(500);
sevenseg(1,0,0,1,1,0,0,1);  //4 
delay(500);
sevenseg(0,0,0,0,0,0,1,0); //0
delay(500);
sevenseg(0,0,0,1,1,1,1,1);  //7
delay(500);
}//over


