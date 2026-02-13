package POO;

public class Moto extends Vehículo{
	private String cilindrada;
	
	public Moto(String modelo, String marca, String cilindrada) {
		super(modelo, marca);
		this.cilindrada = cilindrada;
	}
	public String getCilindrada() {
		return cilindrada;
	}
	public void setCilindrada(String cilindrada) {
		this.cilindrada = cilindrada;
	}
	public void Acelerar() {
		System.out.print("La moto está acelerando");
	}
	public void Frenar() {
		System.out.print("La moto está frenando");
	}
	@Override
	public String toString() {
		return "Moto [" + super.toString() + ", Cilindrada=" + cilindrada + "]";
	}
	
	
	

}
