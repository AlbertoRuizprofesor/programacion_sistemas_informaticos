package poo;

public class Coche extends Vehiculo{
	private String combustible;
	private String StarStop;
	
	public Coche(String modelo, String motor, int ruedas, String color, String marca, String tipo, String combustible, String StarStop) {
		super(modelo, motor, ruedas, color, marca, tipo);
		this.combustible = combustible;
		this.StarStop = StarStop;
	}

	public String getCombustible() {
		return combustible;
	}

	public void setCombustible(String combustible) {
		this.combustible = combustible;
	}

	public String getStarStop() {
		return StarStop;
	}

	public void setStarStop(String starStop) {
		StarStop = starStop;
	}
	
	

	@Override
	public void acelerar() {
		System.out.println("El coche esta acelerando");
	}

	@Override
	public void frenar() {
		// TODO Auto-generated method stub
		super.frenar();
	}

	@Override
	public String toString() {
		return "Coche [combustible=" + combustible + ", StarStop=" + StarStop + ", getCombustible()=" + getCombustible()
				+ ", getStarStop()=" + getStarStop() + ", getModelo()=" + super.getModelo() + ", getMotor()=" + super.getMotor()
				+ ", getRuedas()=" + super.getRuedas() + ", getColor()=" + super.getColor() + ", getMarca()=" + super.getMarca()
				+ ", getTipo()=" + super.getTipo() + ", toString()=" + super.toString() + ", getClass()=" + super.getClass()
				+ ", hashCode()=" + hashCode() + "]";
	}

	

	
	
	
	

}
