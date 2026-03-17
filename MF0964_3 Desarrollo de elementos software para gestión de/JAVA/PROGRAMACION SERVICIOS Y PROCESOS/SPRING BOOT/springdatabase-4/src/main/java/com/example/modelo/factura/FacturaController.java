package com.example.modelo.factura;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/facturas")
public class FacturaController {

    @Autowired
    private FacturaRepository facturaRepository;

    @GetMapping
    public List<Factura> getAllFacturas() {
        return facturaRepository.findAll();
    }

    @GetMapping("/{id}")
    public Optional<Factura> getFacturaById(@PathVariable Integer id) {
        return facturaRepository.findById(id);
    }

    @PostMapping
    public Factura createFactura(@RequestBody Factura factura) {
        return facturaRepository.save(factura);
    }

    @PutMapping("/{id}")
    public Factura updateFactura(@PathVariable Integer id, @RequestBody Factura facturaDetails) {
        return facturaRepository.findById(id).map(factura -> {
            factura.setIdAlumno(facturaDetails.getIdAlumno());
            factura.setImporte(facturaDetails.getImporte());
            factura.setPagado(facturaDetails.getPagado()); // Ahora acepta String
            return facturaRepository.save(factura);
        }).orElseThrow(() -> new RuntimeException("Factura no encontrada con id: " + id));
    }

    @DeleteMapping("/{id}")
    public void deleteFactura(@PathVariable Integer id) {
        facturaRepository.deleteById(id);
    }
}