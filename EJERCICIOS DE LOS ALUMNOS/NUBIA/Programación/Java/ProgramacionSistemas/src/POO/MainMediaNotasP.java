package POO;

public class MainMediaNotasP {
	public static void main(String[] args) {
		MediaNotasP notas=new MediaNotasP();
		
		int[] nota=notas.pedirDatos();
		notas.calculo_notas(nota);
	}

}
