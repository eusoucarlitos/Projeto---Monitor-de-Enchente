// C++ code
//
int Umidade = 0;

void setup()
{
  pinMode(A0, INPUT);
  pinMode(11, OUTPUT);
  pinMode(8, OUTPUT);
}

void loop()
{
  Umidade = analogRead(A0);
  digitalWrite(11, LOW);
  digitalWrite(8, LOW);
  if (Umidade < 100) {
    digitalWrite(11, HIGH);
  } else {
    digitalWrite(8, HIGH);
  }
  delay(10); // Delay a little bit to improve simulation performance
}
