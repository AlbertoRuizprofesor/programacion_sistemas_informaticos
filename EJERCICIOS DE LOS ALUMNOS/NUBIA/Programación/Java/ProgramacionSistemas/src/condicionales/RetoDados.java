package condicionales;
import java.util.Scanner;
import java.util.Random;

public class RetoDados {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		Random dado=new Random();
		
		//BIENVENIDA
		System.out.println("JUEGO DE DADOS");
		System.out.println();
		
		//TURNO JUGADOR
		System.out.print("Pulsa ENTER para lanzar el dado");
		sc.nextLine();
		System.out.println();
		
		//Dado jugador
		int dadojugador = dado.nextInt(6) +1;
		System.out.println("Has sacado un "+dadojugador);
		
		//TURNO MÁQUINA
		
		//Dado máquina
		int dadomaquina = dado.nextInt(6) +1;
		System.out.println("El oponente ha sacado un "+dadomaquina);
		
		//RESULTADOS
		if (dadojugador > dadomaquina) {
			System.out.println();
			System.out.println("¡Has ganado!");
		}
		else if (dadojugador == dadomaquina) {
			System.out.println();
			System.out.println("Empate.");
		}
		else {
			System.out.println();
			System.out.println("Has perdido...");
		}
		sc.close();
		}
			
	}

