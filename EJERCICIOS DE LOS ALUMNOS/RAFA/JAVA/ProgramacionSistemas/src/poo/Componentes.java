package poo;

public class Componentes {
	private String potencia;
	private String tension;
	private String corriente;
	
	public Componentes(String potencia, String tension, String corriente) {
		super();
		this.potencia = potencia;
		this.tension = tension;
		this.corriente = corriente;
	}

	public String getPotencia() {
		return potencia;
	}

	public void setPotencia(String potencia) {
		this.potencia = potencia;
	}

	public String getTension() {
		return tension;
	}

	public void setTension(String tension) {
		this.tension = tension;
	}

	public String getCorriente() {
		return corriente;
	}

	public void setCorriente(String corriente) {
		this.corriente = corriente;
	}

	@Override
	public String toString() {
		return "Componentes [potencia=" + potencia + ", tension=" + tension + ", corriente=" + corriente + "]";
	}
	
	
	
	

}
