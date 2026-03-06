package com.cursos.api.controller;

import com.cursos.api.model.Alumno;
import com.cursos.api.service.AlumnoService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * Capa de Presentación (Controller).
 * Define los endpoints de la API y maneja las peticiones HTTP.
 */
@RestController
@RequestMapping("/api/alumnos")
public class AlumnoController {

    private final AlumnoService alumnoService;

    public AlumnoController(AlumnoService alumnoService) {
        this.alumnoService = alumnoService;
    }

    /**
     * GET /api/alumnos
     * Retorna la lista de todos los alumnos.
     */
    @GetMapping
    public List<Alumno> obtenerTodos() {
        return alumnoService.listarTodos();
    }

    /**
     * GET /api/alumnos/{id}
     * Retorna un alumno por su ID o un error 404 si no existe.
     */
    @GetMapping("/{id}")
    public ResponseEntity<Alumno> obtenerPorId(@PathVariable Long id) {
        return alumnoService.buscarPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
