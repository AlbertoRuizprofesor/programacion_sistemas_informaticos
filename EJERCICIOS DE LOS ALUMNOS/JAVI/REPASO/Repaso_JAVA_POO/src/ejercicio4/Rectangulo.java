package ejercicio4;

public class Rectangulo {

	private double base;
	private double altura;

	public Rectangulo(double base, double altura) {

		this.base = base;
		this.altura = altura;
	}

	public double CalcularArea() {

		return (base * altura) / 2;
	}

	public double CalcularPerimetro() {

		return (base * 2) + (altura * 2);
	}

}
