package Metodos;

public class iva {
	
	public double importe;
		
	public double iva() {
		
		double iva = importe * 0.21;
		
		return iva;
	}
	
	public double total() {
		
		double total = importe + iva();
		
		return total;
		
	}
	
	public void resultados() {
		
		System.out.println("El IVA es: " + iva());
		
		System.out.println("El total es: " + total());
		
	}

}
