$(document).ready(function() {
    $('#login-form').on('submit', function(e) {
        e.preventDefault();
        var username = $('input[name="username"]').val();
        var password = $('input[name="password"]').val();
        var saveLogin = $('input[name="save-login"]').is(':checked');

        if (saveLogin) {
            localStorage.setItem('savedUsername', username);
            localStorage.setItem('savedPassword', password);
        }

        // Redireciona para a rota /link1/ com o username como parâmetro
        window.location.href = "./link1.html?user=" + encodeURIComponent(username);
    });

    // Preencher o formulário automaticamente se as credenciais estiverem salvas
    if (localStorage.getItem('savedUsername') && localStorage.getItem('savedPassword')) {
        $('input[name="username"]').val(localStorage.getItem('savedUsername'));
        $('input[name="password"]').val(localStorage.getItem('savedPassword'));
        $('input[name="save-login"]').prop('checked', true);
    }

    // Função para obter o parâmetro 'user' da URL
    function getUrlParameter(name) {
        name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
        var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
        var results = regex.exec(location.search);
        return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
    }

    var username = getUrlParameter('user');
    if (username) {
        document.getElementById('username').textContent = username;
        
        // Função para buscar os dados do usuário e do score
        function fetchUserData() {
            // Substitua a URL pela URL correta da sua API
            //var apiUrl = `https://davidsousaplay.pythonanywhere.com/users/name/${encodeURIComponent(username)}`;
            
            fetch(apiUrl, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
               
                document.getElementById('score').textContent = data.pontos; // Exibe o valor do campo `pontos`
               })
            .catch(error => {
                console.error('Error fetching user data:', error);
            });
        }
        
        fetchUserData();
    }
});
