#include "HCPCA9685.h"
#define I2CAdd 0x40
HCPCA9685 HCPCA9685(I2CAdd);

#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // set the LCD address to 0x27 for a 16 chars and 2 line display
const int stepPin2 = 10; 
const int dirPin2 = 9; 
const int enPin2 = 8;

const int stepPin1 = 6; 
const int dirPin1 = 5; 
const int enPin1 = 4;

int s_1 = 2000;
int s_2 = 10000;
void setup() {


  lcd.init();
  // Print a message to the LCD.
  lcd.backlight();

  pinMode(stepPin2,OUTPUT); 
  pinMode(dirPin2,OUTPUT);
  pinMode(enPin2,OUTPUT);
  digitalWrite(enPin2,LOW);

  pinMode(stepPin1,OUTPUT); 
  pinMode(dirPin1,OUTPUT);
  pinMode(enPin1,OUTPUT);
  digitalWrite(enPin1,LOW);

    Serial.begin(9600);
    HCPCA9685.Init(SERVO_MODE);
    HCPCA9685.Sleep(false);
    HCPCA9685.Servo(0, 270);  // less back high front // lower // 290 // 240 //
    HCPCA9685.Servo(1, 100);  // high up low down // mid // 100 // 140 //
    HCPCA9685.Servo(2, 120);  // low open high close// grip // 120 open // 160 close



}
  

void loop() {

if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    input.trim();
    
if (input.equalsIgnoreCase("1")) {
  lcd.setCursor(0,0);
  lcd.print("PICKING UP");
  delay(500);
  digitalWrite(dirPin2,LOW); // Enables the motor to move in a particular direction
  for(int x = 0; x < 700; x++) {
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(s_1); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(s_1); }
  delay(2000);
  smoothMovement(2, 120, 180, 10); // GRIP CLOSE 
  smoothMovement(1, 100, 140, 10); // MID
  smoothMovement(0, 270, 240, 10); // BASE
  
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("PICKED");
  
delay(2000);
digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
for(int x = 0; x < 50; x++) {
digitalWrite(stepPin1,HIGH); 
delayMicroseconds(s_2); 
digitalWrite(stepPin1,LOW); 
delayMicroseconds(s_2); }
delay(2000);
smoothMovement(0, 240, 270, 10); // BASE
smoothMovement(1, 140, 100, 10); // MID
smoothMovement(2, 180, 120, 10); // GRIP CLOSE 
lcd.clear();
lcd.print("PLACED");
delay(2000);
smoothMovement(2, 120, 180, 10); // GRIP CLOSE 
smoothMovement(1, 100, 140, 10); // MID
smoothMovement(0, 270, 240, 10); // BASE
delay(2000);
digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
for(int x = 0; x < 50; x++) {
digitalWrite(stepPin1,HIGH); 
delayMicroseconds(s_2); 
digitalWrite(stepPin1,LOW); 
delayMicroseconds(s_2); }
delay(2000);
smoothMovement(0, 240, 270, 10); // BASE
smoothMovement(1, 140, 100, 10); // MID
smoothMovement(2, 180, 120, 10); // GRIP CLOSE 
delay(2000);
digitalWrite(dirPin2,HIGH); // Enables the motor to move in a particular direction
  for(int x = 0; x < 700; x++) {
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(s_1); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(s_1); }
    lcd.clear();
    
        Serial.println("Finished");
        Serial.println();
}

if (input.equalsIgnoreCase("2")) {
delay(500);
  lcd.setCursor(0,0);
  lcd.print("PICKING UP");
  delay(500);
  digitalWrite(dirPin2,LOW); // Enables the motor to move in a particular direction
  for(int x = 0; x < 700; x++) {
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(s_1); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(s_1); }
delay(2000);
smoothMovement(2, 120, 180, 10); // GRIP CLOSE 
smoothMovement(1, 100, 140, 10); // MID
smoothMovement(0, 270, 240, 10); // BASE
delay(2000);
  lcd.clear();
  lcd.setCursor(0,0);
  lcd.print("PICKED");
digitalWrite(dirPin1,HIGH); // Enables the motor to move in a particular direction
for(int x = 0; x < 50; x++) {
digitalWrite(stepPin1,HIGH); 
delayMicroseconds(s_2); 
digitalWrite(stepPin1,LOW); 
delayMicroseconds(s_2); }
delay(2000);
smoothMovement(0, 240, 270, 10); // BASE
smoothMovement(1, 140, 100, 10); // MID
smoothMovement(2, 180, 120, 10); // GRIP CLOSE 
delay(2000);
lcd.clear();
lcd.print("PLACED");
delay(2000);
smoothMovement(2, 120, 180, 10); // GRIP CLOSE 
smoothMovement(1, 100, 140, 10); // MID
smoothMovement(0, 270, 240, 10); // BASE
delay(2000);
digitalWrite(dirPin1,LOW); // Enables the motor to move in a particular direction
for(int x = 0; x < 50; x++) {
digitalWrite(stepPin1,HIGH); 
delayMicroseconds(s_2); 
digitalWrite(stepPin1,LOW); 
delayMicroseconds(s_2); }
delay(2000);
smoothMovement(0, 240, 270, 10); // BASE
smoothMovement(1, 140, 100, 10); // MID
smoothMovement(2, 180, 120, 10); // GRIP CLOSE 
delay(2000);
  digitalWrite(dirPin2,HIGH); // Enables the motor to move in a particular direction
  for(int x = 0; x < 700; x++) {
    digitalWrite(stepPin2,HIGH); 
    delayMicroseconds(s_1); 
    digitalWrite(stepPin2,LOW); 
    delayMicroseconds(s_1); }

        lcd.clear();
        Serial.println("Finished");
        Serial.println();
}





    }
}

void smoothMovement(int servoNumber, int startAngle, int endAngle, int delayTime) {
  int step = (startAngle < endAngle) ? 1 : -1; 

  for (int angle = startAngle; angle != endAngle; angle += step) 
  {
    HCPCA9685.Servo(servoNumber, angle);
    delay(delayTime);
  }

  HCPCA9685.Servo(servoNumber, endAngle);  
  delay(1000); 

  }

