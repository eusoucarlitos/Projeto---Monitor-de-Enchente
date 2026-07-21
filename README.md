# 🌊 Sistema de Monitoramento de Nível da Água para Prevenção de Enchentes

## Geral do Aplicativo:
-  Este aplicativo foi desenvolvido para monitorar o nível da água em áreas suscetíveis a enchentes. O sistema detecta alterações no nível da água e envia alertas aos usuários quando há risco de inundação, permitindo que medidas preventivas sejam tomadas com antecedência;
-  Em poucas palavras, um monitor de enchente.
  
## Componentes utilizados e necessários:
- Arduino Uno R3 - Físico/Online;
- Um computador para enviar o código para o arduino e instalar a interface WEB.

## Arquivos necessários:
### Arduino:
* Arduino pelo Tinkercard: [SensorUmidade - Tinkercard](https://www.tinkercad.com/things/2vFZVZpT9EA-monitor-de-enchente?sharecode=XCLFaeLTbYF_APDIHi28YwsxTJyIfBrj8DvS4ARhXhg)
* Físico (Para Comprar): ["Kit Arduino Start" - ELETROGATE](https://www.eletrogate.com/kit-arduino-start?utm_source=Site&utm_medium=GoogleMerchant&utm_campaign=GoogleMerchant&gad_source=4&gad_campaignid=23952903735&gbraid=0AAAAADqxjs-XIeWP-YSaZxfLFrvQJx7ho&gclid=Cj0KCQjw9ZLSBhCcARIsAEhGKgN1l-aSubWQJe7-Aqt1lGT3C1Jk2ywa5hXJuTF-WEz076K30G8s2QMaAgxtEALw_wcB)

### Backend (API):
* `app.py`
* `sensor.py`
* `LED.py`
### Interface Web:
* `index.html`
* `script.js`
* `styles.css`

## Como funciona:
De Forma simplificada, o programa que consiste no monitoriamento da água das chuvas. Ele avisa ao cliente quando a água está em uma altura com possibilidade de enchete e alertar a ele.

1. O sensor de nível de água monitora continuamente a quantidade de água presente em um determinado local;
2. Os dados capturados são processados pelo sistema desenvolvido em Python;
3. Quando o nível da água ultrapassa o limite considerado seguro, um alerta é acionado;
4. O LED é ligado para indicar visualmente o risco de enchente;
5. O usuário recebe a notificação e pode tomar as medidas de segurança necessárias.

## Bibliotecas usadas / Linguagens usadas:
- `Python`, `Java-script`, `HTML`, `CSS`, `C++`

## Contribuições / Agradecimentos:
----| Projeto desenvolvido com a participação de:
* Carlito
* Ronald (Enzzo)
* Matheus
* Nunes
* Milly (Emilly)
*
* Agradecemos a todos os colaboradores extras que contribuíram para o desenvolvimento deste sistema de prevenção de enchentes.
