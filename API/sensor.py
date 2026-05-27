from flask import Flask, render_template, jsonify, request
from datetime import datetime

class sensorAgua: 
    def __init__ (self, nome, altAtual, altLimite):
        self._nome = nome
        self._altAtual = altAtual
        self._altLimite = altLimite

    def getNome(self):
        return self._nome
    
    def LerAgua(self):
        return self._altAtual

    
    def Analise(self):
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
        print("Olá, informe todas as medidas em CM, por favor.")
        a = float(input("Qual é o nível de água atual da região?"))
        b = float(input("Qual é o nível de água registrado anteriormente da região?"))
        c = float(input("Qual é o limite da região?"))
        Sensor01 = Sensoragua("Caixa", a, b, c)
        Sensor01.Analise()

# Parte em Flask, na teoria

app = Flask(__name__)

# GET = Pegar dodos do site
# POST = Enviar dados
# rotas = o principal/algo/_algo_

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/analise", methods=["GET", "POST"])
def analise():
    if request.method == "POST":
        Altura_Atual = request.form ['Atual']
        Altura_Limite = request.form ['Limite']

        sensor = (
            "Nível",
            Altura_Atual,
            Altura_Limite
        )
        Dado = sensor.Analise()
        
        return f"Dado enviado, resposta: {Dado}"

#Iniciar a host + servidor local
if __name__ == "__main__":
    app.run()
