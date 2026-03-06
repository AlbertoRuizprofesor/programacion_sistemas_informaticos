package com.cursos.api.service;

import com.cursos.api.model.Alumno;
import com.cursos.api.repository.AlumnoRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

/**
 * Capa de Negocio (Service).
 * Aquí se gestiona la lógica de la aplicación y se comunica con el Repositorio.
 */
@Service
public class AlumnoService {

    private final AlumnoRepository alumnoRepository;

    // Inyección por constructor (recomendado por Spring)
    public AlumnoService(AlumnoRepository alumnoRepository) {
        this.alumnoRepository = alumnoRepository;
    }

    public List<Alumno> listarTodos() {
        return alumnoRepository.findAll();
    }

    public Optional<Alumno> buscarPorId(Long id) {
        return alumnoRepository.findById(id);
    }
}
