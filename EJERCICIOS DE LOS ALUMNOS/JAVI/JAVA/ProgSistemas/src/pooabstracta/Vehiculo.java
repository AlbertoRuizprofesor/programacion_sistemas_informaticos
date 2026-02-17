package pooabstracta;

abstract class Vehiculo {
	
	private String nombre;
	private String color;
	private int ruedas;
	private String modelo;
	
	public Vehiculo(String color, int ruedas, String modelo) {
		
		this.color = color;
		this.ruedas = ruedas;
		this.modelo = modelo;
	}

	public String getColor() {
		return color;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	public void setColor(String color) {
		this.color = color;
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
	
	abstract void acelerar();
	abstract void frenar();
	abstract void aparcar();
	
	
	@Override
	public String toString() {
		return "Vehiculo [Color=" + getColor() + ", Ruedas=" + getRuedas() + ", Modelo=" + getModelo()
				+ "]";
	}
	
	
	
	
	

}
