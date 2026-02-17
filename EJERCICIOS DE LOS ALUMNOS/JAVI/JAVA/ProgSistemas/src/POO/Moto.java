package POO;

public class Moto extends Vehiculo {

	private String cilindrada;

	public Moto(String motor, int ruedas, String modelo, double precio, String cilindrada) {
		super(motor, ruedas, modelo, precio);
		this.cilindrada = cilindrada;
	}

	public String getCilindrada() {
		return cilindrada;
	}

	public void setCilindrada(String cilindrada) {
		this.cilindrada = cilindrada;
	}
	
	@Override
	public void acelerar() {
		System.out.println("La moto acelera.");
	}
	
	@Override
	public void frenar() {
		System.out.println("La moto frena.");
	}

	@Override
	public String toString() {
		return "Moto [Cilindrada=" + getCilindrada() + ", Motor=" + getMotor() + ", Ruedas="
				+ getRuedas() + ", Modelo=" + getModelo() + ", Precio=" + getPrecio() + "]";
	}
	
	
	
	
	
	
}
