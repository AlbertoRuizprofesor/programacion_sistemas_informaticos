package POOVIDEOJUEGOS;

public class Lorthemartheron extends worldofwarcraft{
	
	private String choque_arcano;
	private String quemadura_mana;
	
	
	public Lorthemartheron(String vida, String fuerza, String faccion, String choque_arcano, String quemadura_mana) {
		super(vida, fuerza, faccion);
		this.choque_arcano = choque_arcano;
		this.quemadura_mana = quemadura_mana;
	}
	public String getChoque_arcano() {
		return choque_arcano;
	}
	public void setChoque_arcano(String choque_arcano) {
		this.choque_arcano = choque_arcano;
	}
	public String getQuemadura_mana() {
		return quemadura_mana;
	}
	public void setQuemadura_mana(String quemadura_mana) {
		this.quemadura_mana = quemadura_mana;
	}
	@Override
	public void intelecto() {
		System.out.println("su intelecto es 75%");
		
	}
	@Override
	public String toString() {
		
		return super.toString()+
				"Lorthemartheron [choque_arcano=" + choque_arcano + ", quemadura_mana=" + quemadura_mana + "]";
	}
	
	
	
	

}
