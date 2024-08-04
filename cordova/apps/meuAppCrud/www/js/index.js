document.addEventListener('deviceready', function () {
    console.log('Device is ready');

    var db = window.sqlitePlugin.openDatabase({name: 'my.db', location: 'default'});

    db.transaction(function (tx) {
        tx.executeSql('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)', [], function(tx, res) {
            console.log('Table created successfully');
        }, function(tx, error) {
            console.log('Error creating table: ' + error.message);
        });
    });

    // Função para adicionar um novo usuário
    function addUser(name, age) {
        console.log('Adding user:', name, age);
        db.transaction(function (tx) {
            tx.executeSql('INSERT INTO Users (name, age) VALUES (?, ?)', [name, age], function(tx, res) {
                console.log('User added successfully');
            }, function(tx, error) {
                console.log('Error adding user: ' + error.message);
            });
        });
    }

    // Função para listar todos os usuários
    function listUsers() {
        db.transaction(function (tx) {
            tx.executeSql('SELECT * FROM Users', [], function (tx, rs) {
                console.log('Users retrieved: ' + rs.rows.length);
                for (var i = 0; i < rs.rows.length; i++) {
                    console.log('User: ' + rs.rows.item(i).name + ', Age: ' + rs.rows.item(i).age);
                }
            }, function (tx, error) {
                console.log('SELECT SQL statement ERROR: ' + error.message);
            });
        });
    }

    // Adicionando eventos aos botões para adicionar e listar usuários
    document.getElementById('addUserButton').addEventListener('click', function () {
        console.log('Add User button clicked');
        var name = document.getElementById('userName').value;
        var age = document.getElementById('userAge').value;
        addUser(name, age);
    });

    document.getElementById('listUsersButton').addEventListener('click', function () {
        console.log('List Users button clicked');
        listUsers();
    });
});
