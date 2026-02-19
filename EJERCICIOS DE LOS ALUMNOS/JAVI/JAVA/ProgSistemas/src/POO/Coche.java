package POO;

public class Coche extends Vehiculo {
	
	private boolean seguro;

	public Coche(String motor, int ruedas, String modelo, double precio, boolean seguro) {
		super(motor, ruedas, modelo, precio);
		this.seguro = seguro;
	}

	public boolean isSeguro() {
		return seguro;
	}

	public void setSeguro(boolean seguro) {
		this.seguro = seguro;
	}

	@Override
	public void acelerar() {
		System.out.println("El coche acelera.");
	}
	
	@Override
	public void frenar() {
		System.out.println("El coche frena.");
	}

	@Override
	public String toString() {
		return "Coche [Seguro=" + isSeguro() + ", Motor=" + getMotor() + ", Ruedas=" + getRuedas()
				+ ", Modelo=" + getModelo() + ", Precio=" + getPrecio() + "]";
	}
	
	
	
	
	
	
	
	

}
