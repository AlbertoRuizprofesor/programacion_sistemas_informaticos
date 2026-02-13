package condicionales;

public class Notas {
	public static void main(String[] args) {
		
		System.out.println("RESULTADO DE NOTAS");
		
		
		int nota=9;
		
		if(nota<5) {
			System.out.println("Estás suspenso");
			
		}else if(nota<6) {
			System.out.println("Tienes un 5");
		
		}else {
			System.out.printf("Has sacado un %d.", nota);
		}
	}

}
