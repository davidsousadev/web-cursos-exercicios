package com.exemplo.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

@RestController
public class HelloController {

    private final DataSource dataSource;

    public HelloController(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @GetMapping("/test-connection")
    public String testConnection() {
        try (Connection connection = dataSource.getConnection()) {
            return "Conexão bem-sucedida ao banco de dados! URL: " + connection.getMetaData().getURL();
        } catch (SQLException e) {
            return "Falha ao conectar ao banco de dados: " + e.getMessage();
        }
    }
}
