package interfacesImplements;


public class Empresa extends Clientes{

	private String tipo;
		
	public Empresa(String nombre,String tipo) {
		super(nombre);
		this.tipo=tipo;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	@Override
	public String mostrarDatos(String nombre) {
		return super.mostrarDatos(nombre);
	}
	public String mostrarDatos(String nombre, String tipo) {
		return super.mostrarDatos(nombre)+" "+tipo;
	}

	@Override
	public String pagar(String nombre) {
		return "La empresa "+super.pagar(nombre);
		}
}
