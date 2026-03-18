package com.example.modelo.curso;



import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/cursos")
public class CursoController {

    @Autowired
    private CursoRepository cursosRepository;

    @GetMapping
    public List<Curso> getAll() {
        return cursosRepository.findAll();
    }

    @GetMapping("/{id}")
    public Optional<Curso> getById(@PathVariable Integer id) {
        return cursosRepository.findById(id);
    }

    @PostMapping
    public Curso create(@RequestBody Curso curso) {
        return cursosRepository.save(curso);
    }

    @PutMapping("/{id}")
    public Curso update(@PathVariable Integer id, @RequestBody Curso cursoDetails) {
        return cursosRepository.findById(id).map(cursos -> {
            Curso cursosDetails = null;
			cursos.setNombreCurso(cursosDetails.getNombreCurso());
            cursos.setDescripcion(cursosDetails.getDescripcion());
            cursos.setPrecio(cursosDetails.getPrecio());
            return cursosRepository.save(cursos);
        }).orElseThrow(() -> new RuntimeException("Cursos no encontrado"));
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable Integer id) {
        cursosRepository.deleteById(id);
    }
}