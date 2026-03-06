package com.cursos.api.model;

import jakarta.persistence.*;
import lombok.Data;
import java.math.BigDecimal;

@Entity
@Table(name = "facturas")
@Data
public class Factura {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_factura") // Mapeo exacto del nombre en la DB
    private Integer idFactura;

    @Column(name = "id_alumno")
    private Integer idAlumno;

    private BigDecimal importe; // Usamos BigDecimal para dinero (buena práctica)

    private String pagado; // Recibirá 'si' o 'no' desde el ENUM de MariaDB
}