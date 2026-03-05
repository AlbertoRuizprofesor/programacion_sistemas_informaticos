package com.cursos.api.model;

import jakarta.persistence.*;
import lombok.Data;

@Entity
@Table(name = "profesores")
@Data // Genera getters, setters, toString, etc.
public class Profesor {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id; // En tu SQL es INT(11)

    private String nombre;
    private String apellidos;
    private String domicilio;
    private String ciudad;
    private String provincia;
    private String cp;

    @Column(unique = true)
    private String email;
}