package POOAbs;

public class Lavadora extends Electrodoméstico {
	private String carga;
	private double kilos;
	
	public Lavadora(String color, double peso, String marca, String fabricante, double precio, 
			String carga, double kilos) {
		super(color, peso, marca, fabricante, precio);
		this.carga=carga;
		this.kilos=kilos;
	}
	public String getCarga() {
		return carga;
	}
	public void setCarga(String carga) {
		this.carga=carga;
	}
	public double getKilos() {
		return kilos;
	}
	public void setKilos(double kilos) {
		this.kilos=kilos;
	}
	@Override
	public void encender() {
		System.out.println("Encendiendo lavadora");
	}
	@Override
	public void apagar() {
		System.out.println("Apagando lavadora");
	}
	@Override
	public void comprar() {
		System.out.println("Lavadora comprada");
	}
	@Override
	public void devolver() {
		System.out.println("Lavadora en proceso de devolución");
	}
	@Override
	public String toString() {
		return "Lavadora ["+super.toString() + ", carga="+carga+", kilos="+kilos+"]";
	}	
}