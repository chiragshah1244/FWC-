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
  //d2 = ((!q1&&x)||(q0&&x));
  //d1 =((q1&&!q0)||(!q2&&!q1&&q0&&!x));
  //d0 =((q2)||(!q1&&!q0)||(!q1&&x)||(!q0&&x)||(q1&&q0&&!x));
  //y = ((q2&&!q0&&!x)||(q2&&q0&&x));
  
  d2=((!q1 && x) || (!q2 && q0 && x));
  d1=((!q2 && q1 && !q0) || (!q2 && !q1 && q0 && !x));
  d0=((!q1 && !q0) || (!q1 && x) || (q2 && !q1) || (!q2 && !q0 && x) || (!q2 && q1 && q0 && !x));
  y=((q2 && !q1 && !q0 && !x) || (q2 && !q1 && q0 && x));
  
  digitalWrite(2, d2);
  digitalWrite(3, d1);
  digitalWrite(4, d0);
  digitalWrite(5, y);
  
  digitalWrite(13, HIGH);
  delay(3000);
  digitalWrite(13, LOW);
  delay(3000);
  
}
void setup() {
    pinMode(2, OUTPUT);  //OUTPUT for F
    pinMode(3, OUTPUT);  
    pinMode(4, OUTPUT);
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
  
  
