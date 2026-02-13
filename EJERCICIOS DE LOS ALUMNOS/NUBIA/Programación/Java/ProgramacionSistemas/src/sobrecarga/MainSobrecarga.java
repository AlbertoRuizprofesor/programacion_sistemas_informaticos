package sobrecarga;

public class MainSobrecarga {
	public static void main(String [] args) {
		Sobrecarga sobrecarga1=new Sobrecarga("Nubia", 20);
		Sobrecarga sobrecarga2=new Sobrecarga("Darío");
		Sobrecarga sobrecarga3=new Sobrecarga("Mónica", 47, 1200);
		
		sobrecarga1.mostrar();
		sobrecarga2.mostrar();
		sobrecarga3.mostrar();
	}
}
