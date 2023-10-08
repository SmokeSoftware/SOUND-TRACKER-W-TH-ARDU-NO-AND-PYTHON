
void setup() {
  Serial.begin(9600);

}

void loop() {
  int data = analogRead(A0);

  data = map(data,0,1023,0,100);

  Serial.println(data);
  
  delay(50);

}
