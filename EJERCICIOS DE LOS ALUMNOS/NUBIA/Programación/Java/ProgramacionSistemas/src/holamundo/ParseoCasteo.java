package holamundo;

public class ParseoCasteo {
	public static void main(String[] args) {
		double x;
		x=6.90;
		System.out.println("x = "+x);
		int y=(int)x;
		System.out.println("x en nº entero es "+y);
		
		int n=Integer.parseInt("123");
		Double d=Double.parseDouble("3.14");
		System.out.println("El resultado es "+d);
	}
}
