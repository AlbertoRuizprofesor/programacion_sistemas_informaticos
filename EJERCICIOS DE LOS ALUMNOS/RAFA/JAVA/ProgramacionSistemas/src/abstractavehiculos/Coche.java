package abstractavehiculos;

public class Coche extends Vehiculo {
	private int cilindrada;

	public Coche(String color, int ruedas, String modelo, int cilindrada) {
		super(color, ruedas, modelo);
		this.cilindrada=cilindrada;
	}

	public int getCilindrada() {
		return cilindrada;
	}

	public void setCilindrada(int cilindrada) {
		this.cilindrada = cilindrada;
	}

	@Override
	public String toString() {
		return "Coche [cilindrada=" + cilindrada + ", getCilindrada()=" + getCilindrada() + ", getColor()=" + getColor()
				+ ", getRuedas()=" + getRuedas() + ", getModelo()=" + getModelo() + ", toString()=" + super.toString()
				+ ", getClass()=" + getClass() + ", hashCode()=" + hashCode() + "]";
	}

	@Override
	void acelerar() {
		System.out.println("acelera tio");
		
	}

	@Override
	void frenar() {
		System.out.println("frena tio");
		
	}

	@Override
	void aparcar() {
		System.out.println("aparca tio");
		
	}
}
