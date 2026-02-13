package bucles;

public class Ejercicio1Bucles {
	public static void main(String[] args) {

	System.out.println("BUCLE FOR");
		for (int i=1; i<11;i++) {
			System.out.println(i*2);
		}
	System.out.println("BUCLE WHILE");
		int b=0;
		int c=2;
		while (b<11) {
			b++;
			System.out.println(b*c);
		}
	System.out.println("BUCLE DO WHILE");
	int d = 0;
	int e = 2;
	do {
	    System.out.println(d * e);
	    d++;                       
	} while (d < 11);              
		}
}