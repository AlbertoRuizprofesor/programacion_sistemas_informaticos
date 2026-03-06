package modelo3;

import java.sql.Date;

import javax.persistence.*;

@Entity
@Table(name = "clientes")

public class Clientes {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id") // Cambiar el nombre de la columna aquí
    private int id;

    @Column(name = "nombre")
    private String nombre;
    
    @Column(name = "apellidos")
    private String apellidos;
    
    // Constructor por defecto requerido por Hibernate
    public Clientes() {
    }

    // Constructor para crear un objeto de tipo fabricante con un nombre específico
    public Clientes(String nombre,String apellidos) {
        this.nombre = nombre;
        this.apellidos=apellidos;
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

	public String getApellidos() {
		return apellidos;
	}

	public void setApellidos(String apellidos) {
		this.apellidos = apellidos;
	}

	@Override
	public String toString() {
		return "Clientes [id=" + id + ", nombre=" + nombre + ", apellidos=" + apellidos + "]";
	}

	
    
    
}
