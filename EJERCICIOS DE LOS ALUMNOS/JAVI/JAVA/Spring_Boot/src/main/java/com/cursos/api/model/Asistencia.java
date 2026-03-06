package com.cursos.api.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;

@Entity
@Table(name = "asistencia")
@Data
public class Asistencia {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(name = "id_alumno")
    private Integer idAlumno;

    @Column(name = "id_curso")
    private Long idCurso;

    @Column(name = "fecha_asistencia")
    private LocalDate fechaAsistencia;
}