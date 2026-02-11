package POOVIDEOJUEGOS;

public class Sylvanasbrisaveloz extends worldofwarcraft{
	
	private String daga_sombria;
	private String fuego_fulminante;
	public Sylvanasbrisaveloz(String vida, String fuerza, String faccion, String daga_sombria,
			String fuego_fulminante) {
		super(vida, fuerza, faccion);
		this.daga_sombria = daga_sombria;
		this.fuego_fulminante = fuego_fulminante;
		
	}
	public String getDaga_somrbia() {
		return daga_sombria;
	}
	public void setDaga_somrbia(String daga_somrbia) {
		this.daga_sombria = daga_somrbia;
	}
	public String getFuego_fulminante() {
		return fuego_fulminante;
	}
	public void setFuego_fulminante(String fuego_fulminante) {
		this.fuego_fulminante = fuego_fulminante;
	}
	@Override
	public void intelecto() {
		System.out.println("su intelecto es 30%");
	}
	@Override
	public String toString() {
		
		return super.toString()+
				"Sylvanasbrisaveloz [daga_sombria=" + daga_sombria + ", fuego fulminante=" + fuego_fulminante + "]";
	}
	
	
	
	}
	
	

