const express = require('express');
const cors = require('cors');
const WebSocket = require('ws'); // Importa WebSocket

const app = express();
app.use(cors());
app.use(express.json());

let ultimoWebhook = {}; // Armazena o último webhook recebido

// Configura o WebSocket na mesma porta do servidor HTTP
const server = require('http').createServer(app);
const wss = new WebSocket.Server({ server });

// Evento disparado quando um cliente se conecta ao WebSocket
wss.on('connection', (ws) => {
    console.log('Novo cliente conectado via WebSocket.');
    ws.send(JSON.stringify({ mensagem: 'Conexão WebSocket estabelecida.' }));
});

// Função para enviar dados aos clientes WebSocket conectados
function notificarClientes(dados) {
    wss.clients.forEach((client) => {
        if (client.readyState === WebSocket.OPEN) {
            client.send(JSON.stringify(dados));
        }
    });
}

// Rota para receber o webhook
app.post('/meu-webhook', (req, res) => {
    console.log('Webhook recebido:', req.body);
    ultimoWebhook = req.body;
    notificarClientes(ultimoWebhook); // Notifica os clientes
    res.status(200).send('Webhook processado');
});

// Rota GET para retornar o último webhook
app.get('/dados-webhook', (req, res) => {
    res.json(ultimoWebhook);
});

const PORT = 4000;
server.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
