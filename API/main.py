from flask import Flask, jsonify, request
from sensor import sensorAgua
from LED import LED

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
