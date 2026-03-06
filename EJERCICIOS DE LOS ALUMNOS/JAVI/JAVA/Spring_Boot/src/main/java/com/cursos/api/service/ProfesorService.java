package com.cursos.api.service;

import com.cursos.api.model.Profesor;
import com.cursos.api.repository.ProfesorRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class ProfesorService {

    private final ProfesorRepository profesorRepository;

    public ProfesorService(ProfesorRepository profesorRepository) {
        this.profesorRepository = profesorRepository;
    }

    public List<Profesor> listarTodos() {
        return profesorRepository.findAll();
    }

    public Optional<Profesor> buscarPorId(Integer id) {
        return profesorRepository.findById(id);
    }
}