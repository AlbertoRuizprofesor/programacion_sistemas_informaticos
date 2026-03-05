package poo;

public class Transistores extends Componentes {
	private String tipo;//BJT o MOSFET
	private String encapsulado;//patas o superficie
	
	public Transistores(String potencia, String tension, String corriente, String tipo, String encapsulado) {
		super(potencia, tension, corriente);
		this.tipo=tipo;
		this.encapsulado=encapsulado;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	public String getEncapsulado() {
		return encapsulado;
	}

	public void setEncapsulado(String encapsulado) {
		this.encapsulado = encapsulado;
	}

	@Override
	public String toString() {
		/*return "Transistores [tipo=" + tipo + ", encap=" + encapsulado + ", Potencia()=" + getPotencia()
				+ ", getTension()=" + getTension() + ", Corriente()=" + getCorriente() + ", toString()="
				+ super.toString() + "]";*/
		
		return "TRANSISTORES [" +
        tipo + " " +
        encapsulado + " " +
        getPotencia() + " " +
        getTension() + " " +
        getCorriente() + "]";
	}

	
	

	

	
	
	
	
	
}
