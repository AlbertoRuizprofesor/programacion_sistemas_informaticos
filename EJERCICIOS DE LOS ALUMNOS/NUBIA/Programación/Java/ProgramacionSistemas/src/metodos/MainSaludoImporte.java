package metodos;

public class MainSaludoImporte {
	public static void main(String[] args) {
		
		SaludoImporte sal=new SaludoImporte();
		
		sal.saludar("Nubia");
		
		double iva=sal.iva(100);
		
		System.out.println("El iva es: "+iva);
	}

}
