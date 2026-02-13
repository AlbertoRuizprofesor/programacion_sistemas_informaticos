package interfaces;

public class Calculadora implements Operaciones{
	
	@Override
	public int sumar(int a, int b) {
		return a+b;
	}
	@Override
	public int restar (int a, int b) {
		return a-b;
	}
	@Override
	public int multi (int a, int b) {
		return a*b;
	}	
	@Override
	public int divi (int a, int b){
		return a/b;
	}
	@Override
	public void mostrar(int a, int b) {
		System.out.println("a="+a+" b="+b);
		System.out.println(" La suma es " +sumar(a,b));
		System.out.println(" La resta es " +restar(a,b));
		System.out.println(" La multiplicación es " +multi(a, b));
		System.out.println(" La división es " +divi(a, b));
	}
}
