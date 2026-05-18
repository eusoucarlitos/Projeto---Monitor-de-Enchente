class Sensoragua: 
    def __init__ (self, nome, altAtual, altAnterior, altLimite):
        self._nome = nome
        self._altAtual = altAtual
        self._altAnterior = altAnterior
        self._altLimite = altLimite

    def getNome(self):
        return self._nome
    
    def LerAgua(self):
        return self._altAtual

    
    def Analise(self):
        from datetime import datetime
        hora = datetime.now()
        horaAtual = hora.strftime("%H:%M:%S")
        #Analise sobre se está acima do limite
        if self._altAtual < self._altLimite:
            print(f"A água está abaixo do limite. \nHora: {horaAtual}")
        elif self._altAtual > self._altLimite:
            print(f"A água está acima do limite. \nHora: {horaAtual}")
        else:
            print(f"A água está exatamente no limite. \nHora: {horaAtual}")
        print("---------------")

        diferenca = self._altAtual - self._altAnterior
        if self._altAtual > self._altAnterior:
            print(f"O nível d'água subiu {abs(diferenca)}cm \nHora: {horaAtual}")
        elif self._altAtual < self._altAnterior:
            print(f"O nível d'água desceu {abs(diferenca)}cm \nHora: {horaAtual}")
        else:
            print("O nível d'água está parada")


def IniciarPrograma():
        #print("Olá, informe todas as medidas em CM, por favor.")
        #a = float(input("Qual é o nível de água atual da região?"))
        #b = float(input("Qual é o nível de água registrado anteriormente da região?"))
        #c = float(input("Qual é o limite da região?"))
        a, b, c = 10, 12, 15
        Sensor01 = Sensoragua("Caixa", a, b, c)
        Sensor01.Analise()

IniciarPrograma()
