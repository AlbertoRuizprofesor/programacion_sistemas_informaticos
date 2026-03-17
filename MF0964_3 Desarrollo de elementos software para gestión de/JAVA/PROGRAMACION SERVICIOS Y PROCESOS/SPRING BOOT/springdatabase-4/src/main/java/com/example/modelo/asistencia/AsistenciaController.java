package com.example.modelo.asistencia;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/asistencia")
public class AsistenciaController {

    @Autowired
    private AsistenciaRepository asistenciaRepository;

    @GetMapping
    public List<Asistencia> getAll() {
        return asistenciaRepository.findAll();
    }

    @GetMapping("/{id}")
    public Optional<Asistencia> getById(@PathVariable Integer id) {
        return asistenciaRepository.findById(id);
    }

    @PostMapping
    public Asistencia create(@RequestBody Asistencia asistencia) {
        return asistenciaRepository.save(asistencia);
    }

    @PutMapping("/{id}")
    public Asistencia update(@PathVariable Integer id, @RequestBody Asistencia details) {
        return asistenciaRepository.findById(id).map(asistencia -> {
            asistencia.setIdAlumno(details.getIdAlumno());
            asistencia.setIdCurso(details.getIdCurso());
            asistencia.setFechaAsistencia(details.getFechaAsistencia());
            return asistenciaRepository.save(asistencia);
        }).orElseThrow(() -> new RuntimeException("Asistencia no encontrada"));
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Integer id) {
        asistenciaRepository.deleteById(id);
    }
}