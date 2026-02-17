package pooabstracta;

public class Bici extends Vehiculo {

	private int precio;

	public Bici(String color, String string, int i, int string2) {
		super(color, string, i);
		this.precio = string2;
	}

	public int getPrecio() {
		return precio;
	}

	public void setPrecio(int precio) {
		this.precio = precio;
	}

	void acelerar() {
		System.out.println(getNombre() + " está acelerando");
	}

	void frenar() {
		System.out.println(getNombre() + " está frenando");
	}

	void aparcar() {
		System.out.println(getNombre() + " está aparcando");
	}

	@Override
	public String toString() {
		return "Bici [getPrecio()=" + getPrecio() + ", getColor()=" + getColor() + ", getRuedas()=" + getRuedas()
				+ ", getModelo()=" + getModelo() + "]";
	}

}
