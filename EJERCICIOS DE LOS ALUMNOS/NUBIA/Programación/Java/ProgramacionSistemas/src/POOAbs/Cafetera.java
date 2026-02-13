package POOAbs;

public class Cafetera extends Electrodoméstico {
	private String tipo;
	
	public Cafetera(String color, double peso, String marca, String fabricante, double precio, String tipo) {
		super(color, peso, marca, fabricante, precio);
		this.tipo=tipo;
	}
	public String getTipo() {
		return tipo;
	}
	public void setTipo(String tipo) {
		this.tipo=tipo;
	}
	@Override
	public void encender() {
		System.out.println("Encendiendo cafetera");
	}
	@Override
	public void apagar() {
		System.out.println("Apagando cafetera");
	}
	@Override
	public void comprar() {
		System.out.println("Cafetera comprada");
	}
	@Override
	public void devolver() {
		System.out.println("Cafetera en proceso de devolución");
	}
	@Override
	public String toString() {
		return "Cafetera ["+super.toString() + ", tipo="+tipo+"]";
	}
}