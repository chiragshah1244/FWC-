#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>

//    Can be client or even host   //
#ifndef STASSID
#define STASSID "K"  // Replace with your network credentials
#define STAPSK  "iamroot10"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}
//#include<Arduino.h>
int q0=0,q1=0,q2=0,x=0;   //input
int d0,d1,d2,y;          //output

void fsm_read()
{
  q2 = digitalRead(12);
  q1 = digitalRead(16);
  q0 = digitalRead(17);
  x = digitalRead(18);
}

void fsm_update()
{  
   //with dont care
  d2 = ((!q1&&x)||(q0&&x));
  d1 =((q1&&!q0)||(!q2&&!q1&&q0&&!x));
  d0 =((q2)||(!q1&&!q0)||(!q1&&x)||(!q0&&x)||(q1&&q0&&!x));
  y = ((q2&&!q0&&!x)||(q2&&q0&&x));
  
  //without dont care
  //d2=((!q1 && x) || (!q2 && q0 && x));
  //d1=((!q2 && q1 && !q0) || (!q2 && !q1 && q0 && !x));
  //d0=((!q1 && !q0) || (!q1 && x) || (q2 && !q1) || (!q2 && !q0 && x) || (!q2 && q1 && q0 && !x));
  //y=((q2 && !q0 ) || (q2 && x) || (q1 && q0 && x));  // in 00110 state 11 should detect 
  //y=((q2 && !q0) || (q2 && x));

  digitalWrite(15, d2);
  digitalWrite(5, d1);
  digitalWrite(4, d0);
  digitalWrite(14, y);
  
  digitalWrite(13, HIGH);
  delay(2000);
  digitalWrite(13, LOW);
  delay(2000);
  
}
void setup() {
	OTAsetup();
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
	 OTAloop();
fsm_read();
fsm_update();
    
}
