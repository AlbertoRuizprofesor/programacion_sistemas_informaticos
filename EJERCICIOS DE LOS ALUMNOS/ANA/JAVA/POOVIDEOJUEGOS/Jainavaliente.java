package POOVIDEOJUEGOS;


public class Jainavaliente extends worldofwarcraft{
	
	private String descarga_escarcha;
	private String elemental_agua;
	
	public Jainavaliente(String vida, String fuerza, String faccion, String descarga_escarcha, String elemental_agua) {
		super(vida, fuerza, faccion);
		this.descarga_escarcha = descarga_escarcha;
		this.elemental_agua = elemental_agua;
	}
	public String getDescarga_escarcha() {
		return descarga_escarcha;
	}
	public void setDescarga_escarcha(String descarga_escarcha) {
		this.descarga_escarcha = descarga_escarcha;
	}
	public String getElemental_agua() {
		return elemental_agua;
	}
	public void setElemental_agua(String elemental_agua) {
		this.elemental_agua = elemental_agua;
	}
	@Override
	public void intelecto() {
		System.out.println("su intelecto es 20%");
		
	}
	@Override
	public String toString() {
		
		return super.toString()+
				"jainavaliente [descarga_escarcha=" + descarga_escarcha + ", elemental_agua=" + elemental_agua + "]";
	}
	
}

