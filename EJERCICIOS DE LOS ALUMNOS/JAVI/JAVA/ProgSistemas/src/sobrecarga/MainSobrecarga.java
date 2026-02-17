package sobrecarga;

public class MainSobrecarga {
	
	public static void main(String[] args) {
		
		Sobrecarga sobrecarga1 = new Sobrecarga("Javier" , 20);
		Sobrecarga sobrecarga2 = new Sobrecarga("Javier");
		Sobrecarga sobrecarga3 = new Sobrecarga("Ana", 30, 2500.50);
				
		System.out.print(sobrecarga3.mostrar(null, 0, 0));
		
	}
}
