package modelo2;

import java.sql.Date;

import javax.persistence.*;

@Entity
@Table(name = "producto")

public class Producto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id") // Cambiar el nombre de la columna aquí
    private int id;

    @Column(name = "nombre")
    private String nombre;
    
    
    @Column(name = "precio")
    private double precio;
    
    @Column(name = "codigo_fabricante")
    private int codigo_fabricante;
    

    // Constructor por defecto requerido por Hibernate
    public Producto() {
    }

    // Constructor para crear un objeto de tipo fabricante con un nombre específico
    public Producto(String nombre,double precio, int codigo_fabricante) {
        this.nombre = nombre;
        this.precio=precio;
        this.codigo_fabricante=codigo_fabricante;
    }

    // Getter y setter para el atributo id
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    // Getter y setter para el atributo nombre
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

	public double getPrecio() {
		return precio;
	}

	public void setPrecio(double precio) {
		this.precio = precio;
	}

	public int getCodigo_fabricante() {
		return codigo_fabricante;
	}

	public void setCodigo_fabricante(int codigo_fabricante) {
		this.codigo_fabricante = codigo_fabricante;
	}

	@Override
	public String toString() {
		return "Producto [id=" + id + ", nombre=" + nombre + ", precio=" + precio + ", codigo_fabricante="
				+ codigo_fabricante + "]";
	}

   
    
    
    
}
