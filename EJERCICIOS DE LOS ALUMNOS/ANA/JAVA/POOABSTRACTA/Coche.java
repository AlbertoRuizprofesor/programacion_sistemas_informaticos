package POOABSTRACTA;

public class Coche extends Vehiculo {
	private int cilidrada;

	public Coche(String color, int ruedas, String modelo, int cilidrada) {
		super(color, ruedas, modelo);
		this.cilidrada = cilidrada;
		
	}
	public int getCilidrada() {
		return cilidrada;
	}
	public void setCilidrada(int cilidrada) {
		this.cilidrada = cilidrada;
	
	}
	@Override
	public String toString() {
	return "Coche [cilidrada=" + cilidrada + ", getColor()=" + getColor() + ", getRuedas()=" + getRuedas()
			+ ", getModelo()=" + getModelo() + ", toString()=" + super.toString() + ", getClass()=" + getClass()
			+ ", hashCode()=" + hashCode() + "]";
	
	}
	@Override
	void acelerar() {
		System.out.println("¡A tope!");
		
		
	}
	@Override
	void frenar() {
		System.out.println("o frenas o te reviento a bollazos...");
	
	}
	@Override
	void aparcar() {
		System.out.println("ten cuidado al aparcar");
	}
		
	
}





	

	
	
	
	
	

	

	