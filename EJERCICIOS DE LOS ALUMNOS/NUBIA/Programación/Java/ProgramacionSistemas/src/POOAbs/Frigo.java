package POOAbs;

public class Frigo extends Electrodoméstico{
	private String capacidad;
	private double altura;
	
	public Frigo(String color, double peso, String marca, String fabricante, double precio, String capacidad, double altura) {
		super(color, peso, marca, fabricante, precio);
		this.capacidad=capacidad;
		this.altura=altura;
	}
	public String getCapacidad() {
		return capacidad;
	}
	public void setCapacidad(String capacidad) {
		this.capacidad=capacidad;
	}
	public double getAltura() {
		return altura;
	}
	public void setAltura(double altura) {
		this.altura=altura;
	}
	@Override
	public void encender() {
		System.out.println("Encendiendo frigorífico");
	}
	@Override
	public void apagar() {
		System.out.println("Apagando frigorífico");
	}
	@Override
	public void comprar() {
		System.out.println("frigorífico comprado");
	}
	@Override
	public void devolver() {
		System.out.println("frigorífico en proceso de devolución");
	}
	@Override
	public String toString() {
		return "Frigorífico ["+super.toString() + ", capacidad="+capacidad+", altura="+altura+"]";
	}
}
