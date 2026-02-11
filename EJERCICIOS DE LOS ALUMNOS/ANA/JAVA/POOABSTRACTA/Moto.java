package POOABSTRACTA;

public class Moto{
	private String retrovisor;
	private int ruedas;
	private String motor;
	private String manillar;
	public Moto(String retrovisor, int ruedas, String motor, String manillar) {
		super();
		this.retrovisor = retrovisor;
		this.ruedas = ruedas;
		this.motor = motor;
		this.manillar = manillar;
	}
	public String getRetrovisor() {
		return retrovisor;
	}
	public void setRetrovisor(String retrovisor) {
		this.retrovisor = retrovisor;
	}
	public int getRuedas() {
		return ruedas;
	}
	public void setRuedas(int ruedas) {
		this.ruedas = ruedas;
	}
	public String getMotor() {
		return motor;
	}
	public void setMotor(String motor) {
		this.motor = motor;
	}
	public String getManillar() {
		return manillar;
	}
	public void setManillar(String manillar) {
		this.manillar = manillar;
	}
	@Override
	public String toString() {
		return "Moto [retrovisor=" + getRetrovisor() +", rueda=" + getRuedas()+", motor=" + motor + ", manillar=" + manillar +"]";
	}
	void acelerar() {
		System.out.println("¡A topeeee!");
	}
	void frenar() {
		System.out.println("Tranquilos, que el seguro está pagado…creo");
	}
	void aparcar() {
		System.out.println("Ten cuidado al aparcar... que la columna no se mueve");
		
	}
	
	}
		
	
