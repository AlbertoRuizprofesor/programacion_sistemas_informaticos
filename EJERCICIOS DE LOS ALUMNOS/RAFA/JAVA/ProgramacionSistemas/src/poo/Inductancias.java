package poo;

public class Inductancias extends Componentes {
	private String tipo;
	private String tolerancia;
	/**
	 * @param potencia
	 * @param tension
	 * @param corriente
	 */
	public Inductancias(String potencia, String tension, String corriente, String tipo, String tolerancia) {
		super(potencia, tension, corriente);
		this.tipo=tipo;
		this.tolerancia=tolerancia;
	}
	/**
	 * @return the tipo
	 */
	public String getTipo() {
		return tipo;
	}
	/**
	 * @param tipo the tipo to set
	 */
	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	/**
	 * @return the tolerancia
	 */
	public String getTolerancia() {
		return tolerancia;
	}
	/**
	 * @param tolerancia the tolerancia to set
	 */
	public void setTolerancia(String tolerancia) {
		this.tolerancia = tolerancia;
	}
	@Override
	public String toString() {
		return "INDUCTANCIAS [" +
		        tipo + " " +
		        tolerancia + " " +
		        getPotencia() + " " +
		        getTension() + " " +
		        getCorriente() + "]";
	}
	
	
	
	
}
