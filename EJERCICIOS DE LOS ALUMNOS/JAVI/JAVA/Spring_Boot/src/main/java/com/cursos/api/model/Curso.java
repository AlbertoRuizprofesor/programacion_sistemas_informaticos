package com.cursos.api.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;

@Entity
@Table(name = "cursos")
@Data
public class Curso {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id; // BIGINT en SQL = Long en Java

    @Column(name = "nombre_curso") // Mapeo para respetar el guion bajo del SQL
    private String nombreCurso;

    private String descripcion;

    private BigDecimal precio; // DECIMAL(10,2) en SQL = BigDecimal en Java
}