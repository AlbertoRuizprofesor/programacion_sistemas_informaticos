package sobrecarga;

public class Sobrecarga {
	private String nombre;
	private int edad;
	private int ingresos;
	
	public Sobrecarga(String nombre, int edad, int ingresos) {
		super();
		this.nombre = nombre;
		this.edad = edad;
		this.ingresos = ingresos;
	}
	

	public Sobrecarga(String nombre, int edad) {
		super();
		this.nombre = nombre;
		this.edad = edad;
	}
	


	public Sobrecarga(String nombre) {
		super();
		this.nombre = nombre;
	}
	



	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public int getEdad() {
		return edad;
	}


	public void setEdad(int edad) {
		this.edad = edad;
	}


	public int getIngresos() {
		return ingresos;
	}


	public void setIngresos(int ingresos) {
		this.ingresos = ingresos;
	}


	public void mostrar(String getNombre, String getEdad, String getIngresos) {
		System.out.println(getNombre()+" "+getEdad()+" "+getIngresos());
}
	public void mostrar() {
		System.out.println(getNombre()+" "+getEdad());
	}
	
	public void mostrar(String nombre) {
		System.out.println(getNombre());
	}
}
	
	
	