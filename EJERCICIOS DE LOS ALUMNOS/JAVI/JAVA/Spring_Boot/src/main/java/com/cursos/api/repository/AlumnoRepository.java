package com.cursos.api.repository;

import com.cursos.api.model.Alumno;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 * Capa de Acceso a Datos (Repository).
 * JpaRepository proporciona métodos como findAll(), findById(), save(), etc.
 */
@Repository
public interface AlumnoRepository extends JpaRepository<Alumno, Long> {
}
