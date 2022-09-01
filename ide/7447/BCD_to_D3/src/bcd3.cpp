#include<Arduino.h>
int Z,Y,X,W;

// the setup function runs once when you press reset or power the board
void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    
    pinMode(6, INPUT);  
    pinMode(7, INPUT); //giving input(SOCKET) to arduo
    pinMode(8, INPUT);
    pinMode(9, INPUT);
    
}

//Code released under GNU GPL.  Free to use for anything.
void disp_7447(int D, int C, int B, int A)
{
  digitalWrite(2, A); //LSB    //value of A will be given to pin 2
  digitalWrite(3, B); 
  digitalWrite(4, C); 
  digitalWrite(5, D); //MSB

}

// the loop function runs over and over again forever
void loop() {
  
W = digitalRead(6); //LSB / value of 6th pin is assigned to W // w is stored in ardno 
X = digitalRead(7);  
Y = digitalRead(8);  
Z = digitalRead(9); //MSB  
  
disp_7447(Z,Y,X,W);        //assigns value

}

//Giving OUTPUT Directly.



