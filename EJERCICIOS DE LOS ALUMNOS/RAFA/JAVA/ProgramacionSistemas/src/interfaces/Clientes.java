package interfaces;

public class Clientes implements DatosPersonales, 
DatosEconomicos {
	private String nombres;
	
	public Clientes(String nombres) {
		this.nombres = nombres;
	}
	public String getNombres() {
		return nombres;
	}
	
	public void setNombres(String nombres) {
		this.nombres = nombres;
	}
	
	@Override
	public String pagar(String nombre) {
		// TODO Auto-generated method stub
		return "Esta pagando "+nombres;
	}
	@Override
	public String enviar_datos(String nombres) {
		
		
		return "Esta enviando datos "+nombres;
	}
	@Override
	public String firmar(String nombres) {
		// TODO Auto-generated method stub
		return "esta firmando "+nombres;
	}
	@Override
	public String mostrar_datos(String nombre) {
		// TODO Auto-generated method stub
		return "Cliente: "+nombre;
	}
	public String mostrar_datos(String nombres, 
			String tipo) {
		// TODO Auto-generated method stub
		return nombres+tipo;
	}

}
