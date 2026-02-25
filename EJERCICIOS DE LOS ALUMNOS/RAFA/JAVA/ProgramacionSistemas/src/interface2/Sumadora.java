package interface2;

public class Sumadora implements Operaciones {
	public int sumar(int a, int b) {
		return a+b;
	}
	public int restar(int a, int b) {
		return a-b;
	}
	public int multi(int a, int b) {
		return a*b;
	}
	public int divi(int a, int b) {
		return a/b;
	}
	public void mostrar(int a, int b) {
		System.out.println("*******************");
		System.out.println("Suma: " + sumar(a,b));
	}
	
}
