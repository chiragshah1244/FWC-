#include<Arduino.h>
int a=13;

void setup()
{
pinMode(a,OUTPUT);

}

void loop()
{
digitalWrite(a,HIGH);

delay(500);
digitalWrite(a,LOW);

delay(500);
}




