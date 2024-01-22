package com.prince.springdemo.student;


import java.util.List;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/v1/students")
public class StudentController {

  public List<String> findAllStudents() {
    return List.of(
      "Pakodtogo",
      "Hello World"
    );
  }

}
