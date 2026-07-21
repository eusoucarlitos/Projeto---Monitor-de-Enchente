// 1. DEFINIÇÃO DA CLASSE DO SENSOR
class SensorUltrassonico {
  private:
    int triggerPin;
    int echoPin;

  public:
    // Construtor: define quais pinos o sensor vai usar
    SensorUltrassonico(int trig, int echo) {
      triggerPin = trig;
      echoPin = echo;
    }

    // Método que calcula a distância
    float obterDistanciaCM() {
      pinMode(triggerPin, OUTPUT);
      digitalWrite(triggerPin, LOW);
      delayMicroseconds(2);
      digitalWrite(triggerPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(triggerPin, LOW);
      pinMode(echoPin, INPUT);
      
      return 0.01723 * pulseIn(echoPin, HIGH);
    }
};

// 2. DEFINIÇÃO DA CLASSE DO LED
class IndicadorLED {
  private:
    int pinoLED;

  public:
    IndicadorLED(int pino) {
      pinoLED = pino;
    }

    void inicializar() {
      pinMode(pinoLED, OUTPUT);
    }

    void ligar() {
      digitalWrite(pinoLED, HIGH);
    }

    void desligar() {
      digitalWrite(pinoLED, LOW);
    }
};

// --- INSTANCIAÇÃO DOS OBJETOS ---
// Criamos os "objetos" reais baseados nas classes acima
SensorUltrassonico sensor(2, 3); 
IndicadorLED ledAlerta(LED_BUILTIN);

void setup() {
  ledAlerta.inicializar(); // O LED se configura sozinho
}

void loop() {
  // O loop principal fica extremamente fácil de ler (parece inglês fluente)
  float nivelAgua = sensor.obterDistanciaCM();

  if (nivelAgua < 150) {
    ledAlerta.ligar();
  }
  if (nivelAgua > 150) {
    ledAlerta.desligar();
  }

  delay(10);
}
