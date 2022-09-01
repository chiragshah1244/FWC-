#include<Arduino.h>
int Z=0,Y=0,X=0,W=0;
int D,C,B,A;
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);  //OUTPUT for 1th F
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(13, OUTPUT); //clock
    
    pinMode(6, INPUT);  //Input for 1th FF 
    pinMode(7, INPUT);  //INPUT for 2nd FF
    pinMode(8, INPUT);  //INPUT for 3rd FF
    pinMode(9, INPUT);  //INPUT for 4th FF
    
}

void disp_7447(int D, int C, int B, int A)
{
  digitalWrite(2, A); //LSB
  digitalWrite(3, B); 
  digitalWrite(4, C); 
  digitalWrite(5, D); //MSB

}
// the loop function runs over and over again forever
void loop() {
  W = digitalRead(6);  // what ever value is there in pin 6 will go to W
  X = digitalRead(7);
  Y = digitalRead(8);
  Z = digitalRead(9);
  
  digitalWrite(13,HIGH);   //clock high
  delay(200);
  
  A= (!Z&&!W)||(!X&&!W&&!Y); 
  B= (W&&!X&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z);       //incrementation 
  C= (W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z);
  D= (W&&X&&Y&&!Z)||(!W&&!X&&!Y&&Z);
  
  disp_7447(D,C,B,A);  
  digitalWrite(13,LOW);   // clock low
  delay(200);
  }
