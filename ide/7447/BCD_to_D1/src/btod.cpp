//Display the BCD code to d
#include<Arduino.h>
// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);   //declearing 2nd pin  as OUTPUT
    pinMode(3, OUTPUT);   //taking output from ardu
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
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
disp_7447(0,1,0,1);   //(D,C,B,A) 
}


//Display the BCD code to d
