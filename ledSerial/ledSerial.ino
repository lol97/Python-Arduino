#define LED 13

void setup() {
  // put your setup code here, to run once:
  pinMode(LED,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    char cmd = Serial.read();
    if(cmd == 'H'){
      digitalWrite(LED,HIGH);
    }
    else if(cmd=='L'){
      digitalWrite(LED,LOW);
    }
  }
}
