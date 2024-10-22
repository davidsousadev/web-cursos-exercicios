const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios'); // Para enviar requisições HTTP
const app = express();

app.use(bodyParser.json());

// Simulando um banco de dados em memória para armazenar as URLs dos webhooks
const webhooksRegistrados = [];

// Endpoint para registrar um webhook
app.post('/registrar-webhook', (req, res) => {
    const { url } = req.body;

    if (!url) {
        return res.status(400).json({ erro: 'URL do webhook é obrigatória' });
    }

    webhooksRegistrados.push(url);
    console.log('Webhook registrado:', url);

    res.status(200).json({ mensagem: 'Webhook registrado com sucesso!' });
});

async function enviarWebhook(evento, dados) {
    console.log('Enviando webhook:', evento, dados);
    for (const url of webhooksRegistrados) {
        try {
            const resposta = await axios.post(url, { evento, dados });
            console.log(`Webhook enviado para ${url} com sucesso!`);
        } catch (erro) {
            console.error(`Erro ao enviar webhook para ${url}:`, erro.message);
        }
    }
}


// Simulação de evento (ex.: novo usuário cadastrado)
app.post('/novo-usuario', (req, res) => {
    const usuario = req.body;

    console.log('Novo usuário cadastrado:', usuario);

    // Enviando webhook para todos os clientes
    enviarWebhook('novo_usuario', usuario);

    res.status(201).json({ mensagem: 'Usuário cadastrado e webhook enviado!' });
});

// Iniciando o servidor
const PORT = 3000;
app.listen(PORT, () => console.log(`Servidor rodando na porta ${PORT}`));
