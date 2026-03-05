package com.cursos.api.service;

import com.cursos.api.model.Asistencia;
import com.cursos.api.repository.AsistenciaRepository;
import org.springframework.stereotype.Service;
import java.util.List;
import java.util.Optional;

@Service
public class AsistenciaService {

    private final AsistenciaRepository asistenciaRepository;

    public AsistenciaService(AsistenciaRepository asistenciaRepository) {
        this.asistenciaRepository = asistenciaRepository;
    }

    public List<Asistencia> listarTodas() {
        return asistenciaRepository.findAll();
    }

    public Optional<Asistencia> buscarPorId(Integer id) {
        return asistenciaRepository.findById(id);
    }
}