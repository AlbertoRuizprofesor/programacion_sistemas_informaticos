package mvcDB;

public class Cliente {

	private int id;
	private int nif;
	private String nombre;
	private String edad;
	
	
	public Cliente(int id, int nif, String nombre, String edad) {
		
		this.id = id;
		this.nif = nif;
		this.nombre = nombre;
		this.edad = edad;
	}


	public int getId() {
		return id;
	}


	public void setId(int id) {
		this.id = id;
	}


	public int getNif() {
		return nif;
	}


	public void setNif(int nif) {
		this.nif = nif;
	}


	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public String getEdad() {
		return edad;
	}


	public void setEdad(String edad) {
		this.edad = edad;
	}	
	
}