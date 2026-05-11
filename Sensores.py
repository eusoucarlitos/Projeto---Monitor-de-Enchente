class Sensor:
    # Classe base para representar qualquer sensor

    def __init__(self, nome, pino, limite_critico=80):
        self._nome = nome
        self._pino = pino
        self._limite_critico = limite_critico
        self._historico = []
        self._ultimo_valor = 0

    def get_nome(self):
        return self._nome

    def get_ultimo_valor(self):
        return self._ultimo_valor

    def adicionar_leitura(self, valor_bruto):
        valor_processado = self._processar_valor(valor_bruto)
        self._ultimo_valor = valor_processado
        self._historico.append({
            'valor': valor_processado,
            'timestamp': self._get_timestamp()
    })
        return valor_processado

    def _processar_valor(self, valor_bruto):
        # Deve ser sobrescrito pelas subclasses
        return valor_bruto
        
    def _get_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%H:%M:%S")
        
    def esta_critico(self):
        return self._ultimo_valor >= self._limite_critico
    
class SensorUmidade(Sensor):
    #Sensor especifico para umidade do solo

    def __init__(self, pino, limite_critico=30):
        super().__init__()
        self._fator_conversao = 100 / 1023

    def _processar_valor(self, valor_bruto):
        # Converte 0-1023 para 0-100%
        umidade = int(valor_bruto * self._fator_conversao)
        return umidade
    def precisa_regar(self):
        return self._ultimo_valor < 20