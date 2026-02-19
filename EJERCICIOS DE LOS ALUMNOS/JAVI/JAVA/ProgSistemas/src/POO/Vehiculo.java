package POO;

public class Vehiculo {
	
	//ATRIBUTOS
	
	private String motor;  
	private int ruedas;
	private String modelo;
	private double precio; 
	
	
	public Vehiculo(String motor, int ruedas, String modelo, double precio) {
		
		this.motor = motor;
		this.ruedas = ruedas;
		this.modelo = modelo;
		this.precio = precio;
	}


	public String getMotor() {
		return motor;
	}


	public void setMotor(String motor) {
		this.motor = motor;
	}


	public int getRuedas() {
		return ruedas;
	}


	public void setRuedas(int ruedas) {
		this.ruedas = ruedas;
	}


	public String getModelo() {
		return modelo;
	}


	public void setModelo(String modelo) {
		this.modelo = modelo;
	}


	public double getPrecio() {
		return precio;
	}


	public void setPrecio(double precio) {
		this.precio = precio;
	}
	
	public void acelerar () {
		System.out.println("El vehiculo está acelerando.");
	}
	
	public void frenar () {
		System.out.println("El vehiculo está frenando.");
	}


	@Override
	public String toString() {
		return "Vehiculo [motor=" + motor + ", ruedas=" + ruedas + ", modelo=" + modelo + ", precio=" + precio + "]";
	}
		
}
