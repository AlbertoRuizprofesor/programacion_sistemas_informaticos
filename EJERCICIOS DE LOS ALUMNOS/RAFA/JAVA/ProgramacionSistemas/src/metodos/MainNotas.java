package metodos;

public class MainNotas {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Notas notas=new Notas();
		int [] nota=notas.pedirDatos();
		notas.calculo_notas(nota);
		
	}

}

