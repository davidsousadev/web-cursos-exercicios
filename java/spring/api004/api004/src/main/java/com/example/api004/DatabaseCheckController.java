package com.example.api004;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
public class DatabaseCheckController {

    private final JdbcTemplate jdbcTemplate;

    @Autowired
    public DatabaseCheckController(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @GetMapping("/checkDatabase")
    public String checkDatabaseConnection() {
        try {
            int result = jdbcTemplate.queryForObject("SELECT 1", Integer.class);
            return "Connected to database! Result: " + result;
        } catch (Exception e) {
            return "Failed to connect to database: " + e.getMessage();
        }
    }
}

