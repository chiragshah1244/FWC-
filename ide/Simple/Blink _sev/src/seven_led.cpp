#include<Arduino.h>
int i;
  void setup()
  {
    pinMode(9, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);  
    pinMode(10,OUTPUT); 
    
    pinMode(11,OUTPUT); //led
    }
void sevenseg(int a,int b,int c,int d,int e,int f,int g,int h)
{
  digitalWrite(9, a); 
  digitalWrite(3, b); 
  digitalWrite(4, c);
  digitalWrite(5, d); 
  digitalWrite(6, e); 
  digitalWrite(7, f);     
  digitalWrite(8, g); 
  digitalWrite(10,h);
  }
  void blink(int n)  //for blinking light
  {
  for (i=1;i<=n;i++)
  {
  digitalWrite(11,HIGH);
  delay(1000/n);
  digitalWrite(11,LOW);
  delay(1000/n);
  }
  }
    
    void loop()
    {
sevenseg(0,0,0,0,0,0,1,0); //0
delay(500);
sevenseg(1,0,0,1,1,1,1,1);  //1;
blink(1); 
delay(500) ; 
sevenseg(0,0,1,0,0,1,0,0);  //2
blink(2);
delay(500);
sevenseg(0,0,0,0,1,1,0,0);  //3 
blink(3);
delay(500);
sevenseg(1,0,0,1,1,0,0,1);  //4 
blink(4);
delay(500);
sevenseg(0,1,0,0,1,0,0,1);  //5
blink(5);
delay(500);
sevenseg(0,1,0,0,0,0,0,1);  //6
blink(6);
delay(500);
sevenseg(0,0,0,1,1,1,1,1);  //7
blink(7);
delay(500);
sevenseg(0,0,0,0,0,0,0,0);  //8
blink(8);
delay(500);
sevenseg(0,0,0,0,1,0,0,1);  //9
blink(9);
delay(500);//

}
