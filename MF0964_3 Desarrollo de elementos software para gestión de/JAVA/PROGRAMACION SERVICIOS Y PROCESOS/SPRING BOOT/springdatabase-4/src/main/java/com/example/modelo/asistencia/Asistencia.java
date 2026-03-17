package com.example.modelo.asistencia;


import jakarta.persistence.*;

@Entity
@Table(name = "asistencia")
public class Asistencia {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id") // <--- Verifica si en MySQL es 'id' o 'id_asistencia'
    private Integer id;

    @Column(name = "id_alumno")
    private Integer idAlumno;

    @Column(name = "id_curso")
    private Integer idCurso;

    @Column(name = "fecha_asistencia")
    private Integer fechaAsistencia;

    public Asistencia() {}

    // Getters y Setters
    public Integer getId() { return id; }
    public void setId(Integer id) { this.id = id; }
    public Integer getIdAlumno() { return idAlumno; }
    public void setIdAlumno(Integer idAlumno) { this.idAlumno = idAlumno; }
    public Integer getIdCurso() { return idCurso; }
    public void setIdCurso(Integer idCurso) { this.idCurso = idCurso; }
    public Integer getFechaAsistencia() { return fechaAsistencia; }
    public void setFechaAsistencia(Integer fechaAsistencia) { this.fechaAsistencia = fechaAsistencia; }
}