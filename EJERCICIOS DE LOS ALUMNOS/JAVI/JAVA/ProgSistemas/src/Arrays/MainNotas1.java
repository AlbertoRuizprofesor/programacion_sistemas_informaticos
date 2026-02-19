package Arrays;

public class MainNotas1 {

	public static void main(String[] args) {
		
		Notas1 gestion = new Notas1();
		
		double [] notasInput = gestion.pedirNotas();
		
		gestion.mostrarResultados(notasInput);

	}

}
