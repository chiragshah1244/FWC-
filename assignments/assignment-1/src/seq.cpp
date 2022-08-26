#include<Arduino.h>
int q0=0,q1=0,q2=0,x=0;   //input
int d0,d1,d2,y;          //output

void fsm_read()
{
  q2 = digitalRead(6);
  q1 = digitalRead(7);
  q0 = digitalRead(8);
  x = digitalRead(9);
}

void fsm_update()
{  
   //without dont care
  //d2 = ((!q1&&x)||(q0&&x));
  //d1 =((q1&&!q0)||(!q2&&!q1&&q0&&!x));
  //d0 =((q2)||(!q1&&!q0)||(!q1&&x)||(!q0&&x)||(q1&&q0&&!x));
  //y = ((q2&&!q0&&!x)||(q2&&q0&&x));
  
  //with dont care
  d2=((!q1 && x) || (!q2 && q0 && x));
  d1=((!q2 && q1 && !q0) || (!q2 && !q1 && q0 && !x));
  d0=((!q1 && !q0) || (!q1 && x) || (q2 && !q1) || (!q2 && !q0 && x) || (!q2 && q1 && q0 && !x));
  //y=((q2 && !q0 ) || (q2 && x) || (q1 && q0 && x));  // in 00110 state 11 should detect 
  y=((q2 && !q0) || (q2 && x));
  digitalWrite(2, d2);
  digitalWrite(3, d1);
  digitalWrite(4, d0);
  digitalWrite(5, y);
  
  digitalWrite(13, HIGH);
  delay(2000);
  digitalWrite(13, LOW);
  delay(2000);
  
}
void setup() {
    pinMode(2, OUTPUT);  //OUTPUT for F1
    pinMode(3, OUTPUT);  //OUTPUT for F1
    pinMode(4, OUTPUT);  //OUTPUT for F1 
    pinMode(5, OUTPUT);  // to led
    
    pinMode(13, OUTPUT); //clock
    
    pinMode(6, INPUT);  //Input for 1th FF 
    pinMode(7, INPUT);  //INPUT for 2nd FF
    pinMode(8, INPUT);  //INPUT for 3rd FF
    pinMode(9, INPUT);  //INPUT +5V OR GRD
    
}


void loop()
 {
fsm_read();
fsm_update();
  
  }
