document.addEventListener('deviceready', function() {
    alert('Device is ready');

    var db = window.sqlitePlugin.openDatabase({ name: 'my.db', location: 'default' });

    // Criar tabela
    db.transaction(function(tx) {
        tx.executeSql('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, value TEXT)', [], function(tx, result) {
            alert('Table created or already exists.');
        }, function(error) {
            alert('Error creating table: ' + error.message);
        });
    });

    // Adicionar ou atualizar item
    document.getElementById('crud-form').addEventListener('submit', function(event) {
        event.preventDefault();
        var id = parseInt(document.getElementById('item-id').value);
        var value = document.getElementById('value').value;

        db.transaction(function(tx) {
            if (id) {
                // Atualizar item
                tx.executeSql('UPDATE items SET value = ? WHERE id = ?', [value, id], function(tx, res) {
                    alert('Item updated successfully');
                    document.getElementById('crud-form').reset();
                    displayItems();
                }, function(error) {
                    alert('Error updating item: ' + error.message);
                });
            } else {
                // Adicionar novo item
                tx.executeSql('INSERT INTO items (value) VALUES (?)', [value], function(tx, res) {
                    alert('Item added successfully');
                    document.getElementById('crud-form').reset();
                    displayItems();
                }, function(error) {
                    alert('Error adding item: ' + error.message);
                });
            }
        });
    });

    // Excluir item
    function deleteItem(id) {
        db.transaction(function(tx) {
            tx.executeSql('DELETE FROM items WHERE id = ?', [id], function(tx, res) {
                alert('Item deleted successfully');
                displayItems();
            }, function(error) {
                alert('Error deleting item: ' + error.message);
            });
        });
    }

    // Exibir itens
    function displayItems() {
        db.transaction(function(tx) {
            tx.executeSql('SELECT * FROM items', [], function(tx, result) {
                var tbody = document.getElementById('items-table').getElementsByTagName('tbody')[0];
                tbody.innerHTML = '';
                for (var i = 0; i < result.rows.length; i++) {
                    var item = result.rows.item(i);
                    var row = tbody.insertRow();
                    row.insertCell().textContent = item.id;
                    row.insertCell().textContent = item.value;
                    var actionsCell = row.insertCell();
                    var editButton = document.createElement('button');
                    editButton.textContent = 'Edit';
                    editButton.onclick = function() {
                        document.getElementById('item-id').value = item.id;
                        document.getElementById('value').value = item.value;
                    };
                    var deleteButton = document.createElement('button');
                    deleteButton.textContent = 'Delete';
                    deleteButton.onclick = function() {
                        deleteItem(item.id);
                    };
                    actionsCell.appendChild(editButton);
                    actionsCell.appendChild(deleteButton);
                }
            }, function(error) {
                alert('Error retrieving items: ' + error.message);
            });
        });
    }

    // Exibir itens na inicialização
    displayItems();
}, false);
