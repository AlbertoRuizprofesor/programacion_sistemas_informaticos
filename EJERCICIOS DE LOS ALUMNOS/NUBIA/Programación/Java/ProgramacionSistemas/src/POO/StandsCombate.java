package POO;

public class StandsCombate extends Stands{
	private String fuerza;
	
	public StandsCombate (String nombre, String usuario, String fuerza) {
		super(nombre, usuario);
		this.fuerza=fuerza;
	}
	public String getFuerza() {
		return fuerza;
	}
	public void setFuerza(String fuerza) {
		this.fuerza=fuerza;
	}
	@Override
	public String toString() {
		return super.toString() + ", Fuerza="+fuerza;
	}
}
