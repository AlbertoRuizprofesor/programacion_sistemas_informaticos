package POO;

public class StandsHabi extends StandsCombate {
	private String habilidad;
	
	public StandsHabi (String nombre, String usuario, String fuerza, String habilidad) {
		super(nombre, usuario, fuerza);
		this.habilidad=habilidad;
	}
	public String getHabilidad() {
		return habilidad;
	}
	public void setHabilidad(String habilidad) {
		this.habilidad=habilidad;
	}
	public String toString() {
		return super.toString() + ", Habilidad="+habilidad;
	}
	

}
