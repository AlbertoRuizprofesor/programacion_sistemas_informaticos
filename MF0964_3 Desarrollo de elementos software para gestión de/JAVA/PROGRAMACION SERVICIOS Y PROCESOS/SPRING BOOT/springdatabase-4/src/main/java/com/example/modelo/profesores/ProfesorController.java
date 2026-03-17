package com.example.modelo.profesores;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/profesores")
public class ProfesorController {

    @Autowired
    private ProfesorRepository profesorRepository;

    @GetMapping
    public List<Profesor> getAll() {
        return profesorRepository.findAll();
    }

    @GetMapping("/{id}")
    public Optional<Profesor> getById(@PathVariable Integer id) {
        return profesorRepository.findById(id);
    }

    @PostMapping
    public Profesor create(@RequestBody Profesor profesor) {
        return profesorRepository.save(profesor);
    }

    @PutMapping("/{id}")
    public Profesor update(@PathVariable Integer id, @RequestBody Profesor p) {
        return profesorRepository.findById(id).map(profesor -> {
            profesor.setNombre(p.getNombre());
            profesor.setApellido(p.getApellido());
            profesor.setCiudad(p.getCiudad());
            profesor.setDomicilio(p.getDomicilio());
            profesor.setProvincia(p.getProvincia());
            profesor.setCp(p.getCp());
            profesor.setEmail(p.getEmail());
            return profesorRepository.save(profesor);
        }).orElseThrow(() -> new RuntimeException("No existe el profesor " + id));
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Integer id) {
        profesorRepository.deleteById(id);
    }
}