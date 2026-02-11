package POOABSTRACTA;

public class Camion extends Vehiculo{
	private String retrovisor;
	private String motor;
	public Camion(String color, int ruedas, String modelo, String retrovisor, String motor) {
		super(color,ruedas,modelo);
		this.retrovisor = retrovisor;
		this.motor = motor;
	}
	public String getRetrovisor() {
		return retrovisor;
	}
	public void setRetrovisor(String retrovisor) {
		this.retrovisor = retrovisor;
	}
	public String getMotor() {
		return motor;
	}
	public void setMotor(String motor) {
		this.motor = motor;
	}
	@Override
	public String toString() {
		return "Camion [color=" + getColor() +", rueda=" + getRuedas()+", modelo=" + getModelo() +", retrovisor=" + retrovisor + ", motor=" + motor + "]";
	}
	@Override
	void acelerar() {
		System.out.println("Va lo mas rapido que puede");
		
	}
	@Override
	void frenar() {
		System.out.println("Esta llegando a sus destino");
		
	}
	@Override
	void aparcar() {
		System.out.println("A aparcado y esta sacando los productos");
	}
	
	
	}
	
	
	

	