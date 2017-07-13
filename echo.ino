
void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int buff[10];
  int cnt = 0;
  while (Serial.available() > 0) {
    buff[cnt++] = Serial.read();
  }
  for (int i = 0; i < cnt; i++) {
    Serial.write(i);
  }
}
