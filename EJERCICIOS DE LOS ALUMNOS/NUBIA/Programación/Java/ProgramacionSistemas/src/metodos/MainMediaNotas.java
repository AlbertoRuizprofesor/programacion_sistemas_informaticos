package metodos;

public class MainMediaNotas {
	public static void main(String[] args) {
		MediaNotas notas=new MediaNotas();
		// Para que las notas se metan en la array que conecta con suma
		int [] nota=notas.pedirDatos();
		notas.calculo_notas(nota);		
	}
}

