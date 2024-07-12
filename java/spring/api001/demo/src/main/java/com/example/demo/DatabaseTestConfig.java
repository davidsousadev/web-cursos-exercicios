package com.exemplo.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import javax.sql.DataSource;
import java.sql.Connection;
import java.sql.SQLException;

@Configuration
public class DatabaseTestConfig {

    @Autowired
    private DataSource dataSource;

    @Bean
    public CommandLineRunner testConnection() {
        return args -> {
            try (Connection connection = dataSource.getConnection()) {
                System.out.println("Conexão bem-sucedida ao banco de dados!");
                System.out.println("URL do banco de dados: " + connection.getMetaData().getURL());
                System.out.println("Nome do driver: " + connection.getMetaData().getDriverName());
            } catch (SQLException e) {
                System.err.println("Falha ao conectar ao banco de dados:");
                e.printStackTrace();
            }
        };
    }
}
