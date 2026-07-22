/*
==========================================================
        SISTEMA DE MONITORAMENTO DE ENCHENTES
==========================================================

Altura total do reservatório: 300 cm
Classificação:

0 - 99 cm      -> Baixo
100 - 199 cm   -> Médio
200 - 300 cm   -> Alto

O Arduino envia os dados em formato JSON.
==========================================================
*/

//==========================================================
// CLASSE DO SENSOR ULTRASSÔNICO
//==========================================================

class SensorUltrassonico {
  private:
    int triggerPin;
    int echoPin;
  public:
    SensorUltrassonico(int trig, int echo) {
      triggerPin = trig;
      echoPin = echo;
      pinMode(triggerPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }

    float obterDistanciaCM() {
      digitalWrite(triggerPin, LOW);
      delayMicroseconds(2);
      digitalWrite(triggerPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(triggerPin, LOW);
      long tempo = pulseIn(echoPin, HIGH);
      float distancia = tempo * 0.0343 / 2;
      return distancia;
    }
};

//==========================================================
// CLASSE DO LED
//==========================================================

class IndicadorLED {
  private:
    int pino;
  public:
    IndicadorLED(int led) {
      pino = led;
    }

    void iniciar() {
      pinMode(pino, OUTPUT);
    }

    void ligar() {
      digitalWrite(pino, HIGH);
    }

    void desligar() {
      digitalWrite(pino, LOW);
    }
};

//==========================================================
// OBJETOS
//==========================================================

// Trigger = 2
// Echo = 3

SensorUltrassonico sensor(2, 3);
IndicadorLED led(LED_BUILTIN);

//==========================================================
// CONSTANTES
//==========================================================

const float ALTURA_TOTAL = 300.0;

//==========================================================
// SETUP
//==========================================================

void setup() {
  Serial.begin(9600);
  led.iniciar();
}

//==========================================================
// LOOP
//==========================================================

void loop() {
  //--------------------------------------------
  // Distância entre sensor e água
  //--------------------------------------------
  float distancia = sensor.obterDistanciaCM();
  //--------------------------------------------
  // Altura da água
  //--------------------------------------------
  float alturaAgua = ALTURA_TOTAL - distancia;
  //--------------------------------------------
  // Evita valores inválidos
  //--------------------------------------------

  if (alturaAgua < 0)
    alturaAgua = 0;
  if (alturaAgua > ALTURA_TOTAL)
    alturaAgua = ALTURA_TOTAL;

  //--------------------------------------------
  // Classificação
  //--------------------------------------------

  String perigo;
  if (alturaAgua < 100) {
    perigo = "Baixo";
    led.desligar();
  }

  else if (alturaAgua < 200) {
    perigo = "Medio";
    led.desligar();
  }

  else {
    perigo = "Alto";
    led.ligar();
  }

  //--------------------------------------------
  // Envia JSON pela Serial
  //--------------------------------------------

  Serial.print("{");
  Serial.print("\"altura\":");
  Serial.print(alturaAgua, 1);
  Serial.print(",");
  Serial.print("\"perigo\":\"");
  Serial.print(perigo);
  Serial.print("\"");
  Serial.print(",");
  Serial.print("\"led\":");
        
  if (alturaAgua >= 200)
    Serial.print("true");
  else
    Serial.print("false");
  Serial.println("}");
  delay(1000);
}

