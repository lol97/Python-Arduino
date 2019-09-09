/*
 *  Code for photoresistor
 *  by: lol97
 *  seri keyes module
 */

// PIN_DATA was the pin that used for comunicate value from sensor
#define PIN_DATA A0
 
void setup() {
  Serial.begin(9600);
}

void loop() {
  //  read data from PIN_DATA
  int pr_val = analogRead(PIN_DATA);
  Serial.print("Nilai Cahaya : ");
  Serial.print("\t");
  Serial.print(pr_val);
  Serial.println(" unit");
}
