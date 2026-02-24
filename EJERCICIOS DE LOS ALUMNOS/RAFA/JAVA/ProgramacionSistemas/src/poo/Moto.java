package poo;

public class Moto extends Vehiculo {
	private String arranque;
	private String luz;
	
	public Moto(String modelo, String motor, int ruedas, String color, String marca, String tipo, String arranque, String luz) {
		super(modelo, motor, ruedas, color, marca, tipo);
		this.arranque=arranque;
		this.luz=luz;
	}
	
	public String getArranque() {
		return arranque;
	}
	public void setArranque(String arranque) {
		this.arranque = arranque;
	}
	public String getLuz() {
		return luz;
	}
	public void setLuz(String luz) {
		this.luz = luz;
	}
	@Override
	public void acelerar() {
		// TODO Auto-generated method stub
		System.out.println("la moto esta acelerando");
	}
	@Override
	public void frenar() {
		// TODO Auto-generated method stub
		super.frenar();
	}
	@Override
	public String toString() {
		return "Moto [arranque=" + arranque + ", luz=" + luz + ", getArranque()=" + getArranque() + ", getLuz()="
				+ getLuz() + ", getModelo()=" + getModelo() + ", getMotor()=" + getMotor() + ", getRuedas()="
				+ getRuedas() + ", getColor()=" + getColor() + ", getMarca()=" + getMarca() + ", getTipo()=" + getTipo()
				+ ", toString()=" + super.toString() + ", getClass()=" + getClass() + ", hashCode()=" + hashCode()
				+ "]";
	}
	
	
	

}
