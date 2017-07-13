
void setup()
{
  Serial.begin(38400);
}

void loop()
{
  byte buff[10];
  int cnt = 0;
  int max_len = 16
  while (Serial.available() > 0 && cnt < max_len) {
    buff[cnt++] = Serial.read();
  }
  Serial.write(buff, max_len);
}
