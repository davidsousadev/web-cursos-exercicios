$(document).ready(function() {
    const apiUrlBase = 'https://davidsousaplay.pythonanywhere.com/users/';

    // Função para extrair parâmetros da URL
    function getParameterByName(name, url = window.location.href) {
        name = name.replace(/[\[\]]/g, '\\$&');
        const regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)');
        const results = regex.exec(url);
        if (!results) return null;
        if (!results[2]) return '';
        return decodeURIComponent(results[2].replace(/\+/g, ' '));
    }

    const username = getParameterByName('user');  // Assumindo que 'user' é o nome do parâmetro na URL

    if (!username) {
        console.error('Username não encontrado na URL');
        return;
    }

    const apiUrl = `${apiUrlBase}name/${username}`;

    // Função para obter pontos do usuário
    function getUserPoints() {
        return fetch(apiUrl)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na resposta da API');
                }
                return response.json();
            })
            .then(data => data.pontos)
            .catch(error => {
                console.error('Erro ao obter pontos do usuário:', error);
                return 0;
            });
    }

    // Função para atualizar pontos do usuário
    function updateUserPoints(newPoints) {
        return fetch(apiUrl, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ pontos: newPoints })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao atualizar pontos do usuário');
            }
            return response.json();
        })
        .catch(error => {
            console.error('Erro ao atualizar pontos do usuário:', error);
        });
    }

    // Função para jogar o jogo automaticamente
    function playGame() {
        const userNumber = Math.floor(Math.random() * 101);
        const machineNumber = Math.floor(Math.random() * 101);

        getUserPoints().then(userPoints => {
            let newPoints;
            let resultMessage;

            if (userNumber > machineNumber) {
                newPoints = userPoints + userNumber;
                resultMessage = `Você ganhou! Seu número: ${userNumber}, Computador: ${machineNumber}. Seus pontos: ${newPoints}`;
            } else {
                newPoints = userPoints - machineNumber;
                resultMessage = `Você perdeu! Seu número: ${userNumber}, Computador: ${machineNumber}. Seus pontos: ${newPoints}`;
            }

            // Atualiza os pontos e exibe o resultado
            updateUserPoints(newPoints).then(() => {
                $('#result').text(resultMessage);
            });
        });
    }

    // Executa o jogo automaticamente ao carregar a página
    playGame();

    // Função para o botão de voltar
    $('#back-button').click(function() {
        // Redireciona para a página principal ou outra rota desejada
        window.location.href = "./link2.html?user=" + encodeURIComponent(username);
    });
    $('#denovo').click(function() {
        // Redireciona para a página principal ou outra rota desejada
        window.location.href = "./sorter.html?user=" + encodeURIComponent(username);
    });
});
