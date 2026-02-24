package poo;

public class Vehiculo {
	private String modelo;
	private String motor;
	private int ruedas;
	private String color;
	private String marca;
	private String tipo;
	
	public Vehiculo(String modelo, String motor, int ruedas, String color, String marca, String tipo) {
		super();
		this.modelo = modelo;
		this.motor = motor;
		this.ruedas = ruedas;
		this.color = color;
		this.marca = marca;
		this.tipo = tipo;
	}

	public String getModelo() {
		return modelo;
	}

	public void setModelo(String modelo) {
		this.modelo = modelo;
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

	public String getColor() {
		return color;
	}

	public void setColor(String color) {
		this.color = color;
	}

	public String getMarca() {
		return marca;
	}

	public void setMarca(String marca) {
		this.marca = marca;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}
	
	public void acelerar() {
		System.out.println("Acelerando");
	}
	public void frenar() {
		System.out.println("Frenando");
	}
	@Override
	public String toString() {
		return "Vehiculo [modelo=" + modelo + ", motor=" + motor + ", ruedas=" + ruedas + ", color=" + color
				+ ", marca=" + marca + ", tipo=" + tipo + "]";
	}
	
	
	
	
	
}