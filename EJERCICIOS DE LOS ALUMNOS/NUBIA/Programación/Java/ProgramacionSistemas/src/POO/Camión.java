package POO;

public class Camión extends Vehículo {
	private String peso;
	
	public Camión (String marca, String modelo, String peso) {
		super(marca, modelo);
		this.peso = peso;
	}
	public String getPeso() {
		return peso;
	}
	public void setPeso(String peso) {
		this.peso=peso;
	}
	public void Acelerar() {
		System.out.println("El camión está acelerando");
	}
	public void Frenar() {
		System.out.println("El camión está frenando");
	}
	@Override
	public String toString() {
		return "Camión ["+ super.toString() + ", Peso=" + peso + "]";
		
	}
}
