package interfacesImplements;

public class Clientes implements DatosPersonales, DatosEconómicos {
	
	private String nombre;
	
	public Clientes(String nombre) {
		super();
		this.nombre=nombre;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
	@Override
	public String enviarDatos(String nombre) {
		return "Está enviando datos, "+nombre;
	}
	
	@Override
	public String firmar(String nombre) {
		return "Está firmando, "+nombre;
	}

	@Override
	public String mostrarDatos(String nombre) {
		// TODO Auto-generated method stub
		return "Cliente: "+nombre;
	}
	
	@Override
	public String pagar(String nombre) {
		return "Está pagando, "+nombre;
	}

}
