// URL DA API

const API = "http://127.0.0.1:5000/api";

// Atualiza os dados na tela

async function atualizarMonitor() {

    try {

        const resposta = await fetch(API);

        const dados = await resposta.json();

        document.getElementById("altura").innerText =
            dados.altura.toFixed(1) + " cm";

        const perigo = document.getElementById("perigo");

        perigo.innerText = dados.perigo;

        // Cores do texto (verde, amarelo e vermelho)

        if (dados.perigo === "Baixo") {

            perigo.style.color = "green";

        }

        else if (dados.perigo === "Médio") {

            perigo.style.color = "#d8a000";

        }

        else {

            perigo.style.color = "red";

        }

    }

    catch (erro) {

        console.log("Erro ao conectar à API.");

    }

}

// Atualização automática

atualizarMonitor();

setInterval(atualizarMonitor, 1000);
