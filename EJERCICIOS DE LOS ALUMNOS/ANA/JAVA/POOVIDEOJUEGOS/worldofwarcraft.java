package POOVIDEOJUEGOS;

public class worldofwarcraft {

	private String vida;
	private String fuerza;
	private String faccion;

	public worldofwarcraft(String vida, String fuerza, String faccion) {
			
			this.vida = vida;
			this.fuerza = fuerza;
			this.faccion = faccion;
		}

	public String getVida() {
		return vida;
	}

	public void setVida(String vida) {
		this.vida = vida;
	}

	public String getFuerza() {
		return fuerza;
	}

	public void setFuerza(String fuerza) {
		this.fuerza = fuerza;
	}

	public void intelecto() {
		System.out.println("maximo de intelecto");
	}

	@Override
	public String toString() {
		return "worldofwarcraft [vida=" + vida + ", fuerza=" + fuerza + ", faccion=" + faccion +"]";
	}

	public String getFaccion() {
		return faccion;
	}

	public void setFaccion(String faccion) {
		this.faccion = faccion;
	}
	
}

