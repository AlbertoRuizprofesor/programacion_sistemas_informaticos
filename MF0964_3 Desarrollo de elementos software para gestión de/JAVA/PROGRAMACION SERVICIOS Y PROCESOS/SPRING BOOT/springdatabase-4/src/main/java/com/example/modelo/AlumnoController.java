package com.example.modelo; // Ajustado a tu paquete actual

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/alumnos")
public class AlumnoController {

    @Autowired
    private AlumnoRepository alumnoRepository;

    // Obtener todos los alumnos de la tabla
    @GetMapping
    public List<Alumno> getAllAlumnos() {
        return alumnoRepository.findAll();
    }

    // Obtener un alumno por ID
    @GetMapping("/{id}")
    public Optional<Alumno> getAlumnoById(@PathVariable Integer id) {
        return alumnoRepository.findById(id);
    }

    // Crear un nuevo alumno
    @PostMapping
    public Alumno createAlumno(@RequestBody Alumno alumno) {
        return alumnoRepository.save(alumno);
    }

    // Actualizar un alumno existente
    @PutMapping("/{id}")
    public Alumno updateAlumno(@PathVariable Integer id, @RequestBody Alumno alumnoDetails) {
        return alumnoRepository.findById(id).map(alumno -> {
            alumno.setNombre(alumnoDetails.getNombre());
            alumno.setApellidos(alumnoDetails.getApellidos());
            alumno.setCiudad(alumnoDetails.getCiudad());
            alumno.setDireccion(alumnoDetails.getDireccion());
            return alumnoRepository.save(alumno);
        }).orElseThrow(() -> new RuntimeException("Alumno no encontrado con id: " + id));
    }

    // Borrar un alumno
    @DeleteMapping("/{id}")
    public void deleteAlumno(@PathVariable Integer id) {
        alumnoRepository.deleteById(id);
    }
}