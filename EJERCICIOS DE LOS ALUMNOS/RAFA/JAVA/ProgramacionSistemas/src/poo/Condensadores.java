package poo;

public class Condensadores extends Componentes {
	private String tipo;//ceramico,electrolitico,tantalio,poliester,mica
	private String polaridad;//polarizados, no polarizados
	/**
	 * @param potencia
	 * @param tension
	 * @param corriente
	 */
	public Condensadores(String potencia, String tension, String corriente, String tipo, String polaridad) {
		super(potencia, tension, corriente);
		this.tipo=tipo;
		this.polaridad=polaridad;
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
	 * @return the polaridad
	 */
	public String getPolaridad() {
		return polaridad;
	}
	/**
	 * @param polaridad the polaridad to set
	 */
	public void setPolaridad(String polaridad) {
		this.polaridad = polaridad;
	}
	@Override
	public String toString() {
		return "CONDENSADORES [" +
		        tipo + " " +
		        polaridad + " " +
		        getPotencia() + " " +
		        getTension() + " " +
		        getCorriente() + "]";
	}
	
	
	
}
