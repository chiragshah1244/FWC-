#include<Arduino.h>
int A=0,B=1,C=0,D=1;
int a,b,c,d,e,f,g;
void setup()
{
 
    pinMode(6,OUTPUT);
    pinMode(7,OUTPUT);
    pinMode(8,OUTPUT);
    pinMode(9,OUTPUT);
    pinMode(10,OUTPUT);
    pinMode(11,OUTPUT);
    pinMode(12,OUTPUT);
}
void convert(int A, int B,int C,int D)
{
 a =(!A&&B&&!C&&!D)||(!A&&!B&&!C&&D);                  // LOGICS without IC
 b=(!A&&B&&!C&&D)||(!A&&B&&C&&!D);
 c=(!A&&!B&&C&&!D);
 d=(!A&&B&&!C&&!D)||(!A&&!B&&!C&&D)||(!A&&B&&C&&D);
 e=(!A&&D)||(!A&&B&&!C)||(!B&&!C&&D);
 f=(!A&&!B&&D)||(!A&&!B&&C)||(!A&&C&&&D);
 g=(!A&&!B&&!C)||(!A&&B&&C&&D);
 
 digitalWrite(6,a);  //what ever the a valve has that is given to pin 6 
 
 digitalWrite(7,b);
 
 digitalWrite(8,c);
 
 digitalWrite(9,d);
 
 digitalWrite(10,e);
 
 digitalWrite(11,f);
 
 digitalWrite(12,g);
}


// the loop function runs over and over again forever
void loop() 
{
  convert(A,B,C,D);
  
}



//without IC 
