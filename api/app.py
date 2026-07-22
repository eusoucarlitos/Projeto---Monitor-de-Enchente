from flask import Flask, jsonify
from flask_cors import CORS

import json
import threading
import time
from datetime import datetime


app = Flask(__name__)
CORS(app)

ARQUIVO_JSON = "dados.json"

# Salva os dados no JSON

def salvar_dados(altura, perigo, led):

    dados = {

        "altura": round(altura,1),

        "perigo": perigo,

        "led": led,

        "ultimaAtualizacao":
        datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    }

    with open(ARQUIVO_JSON,"w",encoding="utf-8") as arquivo:

        json.dump(dados,arquivo,indent=4,ensure_ascii=False)


# Simulação do Tinkercad

altura = 0
subindo = True

def simulacao():

    global altura
    global subindo

    while True:

        if subindo:
            altura += 2
        else:
            altura -= 2

        if altura >= 300:
            subindo = False

        if altura <= 0:
            subindo = True

        if altura < 100:

            perigo = "Baixo"

        elif altura < 200:

            perigo = "Médio"

        else:

            perigo = "Alto"

        led = altura >= 200

        salvar_dados(
            altura,
            perigo,
            led
        )

        time.sleep(1)

# =====================================================
# API
# =====================================================

@app.route("/")
def inicio():

    return {

        "status":"online",

        "mensagem":"API do Monitor de Enchentes"

    }

@app.route("/api")
def api():

    with open(
        ARQUIVO_JSON,
        "r",
        encoding="utf-8"
    ) as arquivo:

        return jsonify(json.load(arquivo))

# MAIN

if __name__ == "__main__":

    thread = threading.Thread(
        target=simulacao
    )

    thread.daemon = True

    thread.start()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
