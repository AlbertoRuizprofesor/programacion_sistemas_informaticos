package com.cursos.api.controller;

import com.cursos.api.model.Asistencia;
import com.cursos.api.service.AsistenciaService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.List;

@RestController
@RequestMapping("/api/asistencia")
public class AsistenciaController { // Puedes renombrar la clase a AsistenciaController

    private final AsistenciaService asistenciaService;

    public AsistenciaController(AsistenciaService asistenciaService) {
        this.asistenciaService = asistenciaService;
    }

    @GetMapping
    public List<Asistencia> obtenerTodas() {
        return asistenciaService.listarTodas();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Asistencia> obtenerPorId(@PathVariable Integer id) {
        return asistenciaService.buscarPorId(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}