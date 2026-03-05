package sobrecarga;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Sobrecarga sobrecarga3=new Sobrecarga("alberto",20,3000);
		Sobrecarga sobrecarga1=new Sobrecarga("alberto",20);
		Sobrecarga sobrecarga2=new Sobrecarga("alberto");
		sobrecarga1.mostrar();
		sobrecarga2.mostrar();
		sobrecarga3.mostrar();
		
	}

}
