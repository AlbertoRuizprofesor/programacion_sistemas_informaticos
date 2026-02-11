package POOVIDEOJUEGOS;

public class Anduinwrynn extends worldofwarcraft {
	
	private String luz_sagrada;
	private String salto_fe;
	
	public Anduinwrynn (String vida, String fuerza, String faccion, String luz_sagrada, String salto_fe) {
	super(vida, fuerza, faccion);
	
	this.luz_sagrada = luz_sagrada;
	this.salto_fe = salto_fe;
	

	}

	public String getLuz_sagrada() {
		return luz_sagrada;
	}

	public void setLuz_sagrada(String luz_sagrada) {
		this.luz_sagrada = luz_sagrada;
	}

	public String getSalto_fe() {
		return salto_fe;
	}

	public void setSalto_fe(String salto_fe) {
		this.salto_fe = salto_fe;
	}
	@Override
	public void intelecto() {
		System.out.println("su intelecto es 50%");
	}
	@Override
	public String toString() {
		
		return super.toString()+
				"Anduinwrynn [luz_sagrada=" + luz_sagrada +", salto_fe=" + salto_fe + "]";
	}
	
}
