package condicionales;
import java.util.Scanner;
import java.util.Random;

public class Dados2 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Random dado=new Random();
		
		System.out.println("JUEGO DE DADOS");
		
		System.out.println("Pulsa ENTER para tirar el dado");
		sc.nextLine();
		
		int tiradaJugador = dado.nextInt(6) +1;
		System.out.println("Has sacado un "+tiradaJugador);
		
		int tiradaMaquina = dado.nextInt(6)+1;
		System.out.println("La máquina ha sacado un "+tiradaMaquina);
		
		if (tiradaJugador > tiradaMaquina) {
			System.out.println("Has ganado");
		}
		else if (tiradaJugador < tiradaMaquina) {
			System.out.println("Has perdido");
		}
		else if (tiradaJugador == tiradaMaquina) {
			System.out.println("Empate");
		}
		sc.close();

		}


}
