package com.example.api003;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class Home {

    @GetMapping("/")
    @ResponseBody
    public String hello() {
        return "Hello, world!";
    }
}
