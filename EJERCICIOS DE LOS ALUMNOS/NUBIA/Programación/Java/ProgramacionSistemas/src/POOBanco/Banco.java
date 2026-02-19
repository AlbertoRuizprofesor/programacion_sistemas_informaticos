package POOBanco;

public class Banco {
	
	private String nombreBanco;
	
	public Banco(String nombreBanco) {
		this.nombreBanco=nombreBanco;
	}
	
	public String getnombreBanco() {
		return nombreBanco;
	}
	
	public void setnombreBanco(String nombreBanco) {
		this.nombreBanco=nombreBanco;
	}
	
	@Override
	public String toString() {
		return "Banco: "+nombreBanco;
	}

}
