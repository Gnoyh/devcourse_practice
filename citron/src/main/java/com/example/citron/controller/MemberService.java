package com.example.citron.controller;

import io.swagger.annotations.ApiOperation;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MemberService {

    @GetMapping("/members")
    @ApiOperation("GET")
    public void get() {

    }

    @PostMapping("/members")
    @ApiOperation("POST")
    public void register() {

    }

    @DeleteMapping("/members")
    @ApiOperation("DELETE")
    public void delete() {

    }
}
