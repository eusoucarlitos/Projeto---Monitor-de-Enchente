class Sensoragua: 
    def __init__ (self, altAtual, altAnterior, altLimite):
        self.altAtual = altAtual
        self.altAnterior = altAnterior
        self.altLimite = altLimite
    
    def LerAgua(self):
        print(self.altAnterior)
        self.altAnterior = self.altAtual
        print(self.altAtual) 

    
    def Analise(self):
        #Analise sobre se está acima do limite
        if self.altAtual < self.altLimite:
            print(f"A água está abaixo do limite: {self.altAtual}:{self.altLimite}")
        elif self.altAtual > self.altLimite:
            print(f"A água está acima do limite: {self.altAtual}:{self.altLimite}")
        else:
            print(f"A água está exatamente no limite: {self.altAtual}:{self.altLimite}")

        Diferenca = self.altAtual - self.altAnterior
        if self.altAtual > self.altAnterior:
            print(f"A água está subindo, teoricamente falando: \nAtual = {self.altAtual}:{self.altAnterior} = Anterior\n Subiu: {Diferenca}cm" )
        elif self.altAtual < self.altAnterior:
            print(f"A água está descendo, teoricamente falando \nAtual = {self.altAtual}:{self.altAnterior} = Anterior\n Desceu: {Diferenca}cm")
        else:
            print("A água está parada, não está subido nem descendo")


def IniciarPrograma():
        print("Olá, informe todas as medidas em CM, por favor.")
        #a = float(input("Qual é o nível de água atual da região?"))
        #b = float(input("Qual é o nível de água registrado anteriormente da região?"))
        #c = float(input("Qual é o limite da região?"))
        a, b, c = 10, 12, 15
        Sensor01 = Sensoragua(a, b, c)
        Sensor01.Analise()

IniciarPrograma()