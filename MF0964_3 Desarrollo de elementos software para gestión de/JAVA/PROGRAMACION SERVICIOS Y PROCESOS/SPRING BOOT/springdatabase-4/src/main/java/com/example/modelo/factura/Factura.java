package com.example.modelo.factura;


import jakarta.persistence.*;

@Entity
@Table(name = "facturas")
public class Factura {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id_factura")
    private Integer idFactura;

    @Column(name = "id_alumno")
    private Integer idAlumno;

    private Double importe;
    
    // Cambiado a String para aceptar 'si' o 'no' de la base de datos
    private String pagado;

    public Factura() {}

    // Getters y Setters
    public Integer getIdFactura() { return idFactura; }
    public void setIdFactura(Integer idFactura) { this.idFactura = idFactura; }

    public Integer getIdAlumno() { return idAlumno; }
    public void setIdAlumno(Integer idAlumno) { this.idAlumno = idAlumno; }

    public Double getImporte() { return importe; }
    public void setImporte(Double importe) { this.importe = importe; }

    public String getPagado() { return pagado; }
    public void setPagado(String pagado) { this.pagado = pagado; }
}