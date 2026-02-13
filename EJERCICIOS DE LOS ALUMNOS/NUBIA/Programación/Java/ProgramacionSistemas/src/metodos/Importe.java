package metodos;

public class Importe {
	
	public double iva(int importe) {
		return (importe*0.21);
	}
	
	public void total(int importe, double iva) {
		System.out.println("El total es: "+(importe+iva));
	}

}
