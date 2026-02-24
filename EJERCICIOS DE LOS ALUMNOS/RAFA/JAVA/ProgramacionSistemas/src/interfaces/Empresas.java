package interfaces;

public class Empresas extends Clientes{

	private String tipo;
	
	public Empresas(String nombres,String tipo) {
		super(nombres);
		this.tipo=tipo;		// TODO Auto-generated constructor stub
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	@Override
	public String mostrar_datos(String nombre, 
			String tipo) {
		// TODO Auto-generated method stub
		return super.mostrar_datos(nombre)+" "+tipo;
	}

	@Override
	public String pagar(String nombre) {
		// TODO Auto-generated method stub
		return "la Empresa "+super.pagar(nombre);
	}
	
}