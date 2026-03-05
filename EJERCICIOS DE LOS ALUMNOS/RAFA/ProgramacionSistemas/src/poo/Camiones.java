package poo;

public class Camiones extends Vehiculo {
	private String tonelaje;
	private String remolque;
	
	public Camiones(String modelo, String motor, int ruedas, String color, String marca, String tipo, String tonelaje, String remolque) {
		super(modelo, motor, ruedas, color, marca, tipo);
		this.tonelaje=tonelaje;
		this.remolque=remolque;
	}

	public String getTonelaje() {
		return tonelaje;
	}

	public void setTonelaje(String tonelaje) {
		this.tonelaje = tonelaje;
	}

	public String getRemolque() {
		return remolque;
	}

	public void setRemolque(String remolque) {
		this.remolque = remolque;
	}
	
	@Override
	public void acelerar() {
		// TODO Auto-generated method stub
		System.out.println("el camion esta acelerando");
	}
	@Override
	public void frenar() {
		// TODO Auto-generated method stub
		super.frenar();
	}

	@Override
	public String toString() {
		return "Camiones [tonelaje=" + tonelaje + ", remolque=" + remolque + ", getTonelaje()=" + getTonelaje()
				+ ", getRemolque()=" + getRemolque() + ", getModelo()=" + super.getModelo() + ", getMotor()=" + super.getMotor()
				+ ", getRuedas()=" + super.getRuedas() + ", getColor()=" + super.getColor() + ", getMarca()=" + super.getMarca()
				+ ", getTipo()=" + super.getTipo() + ", toString()=" + super.toString() + ", getClass()=" + super.getClass()
				+ ", hashCode()=" + hashCode() + "]";
	}
	
	
	
	
}
