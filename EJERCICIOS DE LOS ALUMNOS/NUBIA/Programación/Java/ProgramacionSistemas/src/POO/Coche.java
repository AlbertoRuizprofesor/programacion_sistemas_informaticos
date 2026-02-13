package POO;

public class Coche extends Vehículo {
	private String color;
	
	public Coche(String marca, String modelo, String color) {
		super(marca, modelo);
		this.color=color;
	}
	public String getAño() {
		return color;
	}
	public void setAño(String año) {
		this.color = año;
	}
	public void acelerar() {
		System.out.println("El coche está acelerando");
	}
	public void frenar() {
		System.out.println("El coche está frenando");
	}
	@Override
	public String toString() {
		return "Coche [" + super.toString() + ", color=" + color + "]";
	}
}
