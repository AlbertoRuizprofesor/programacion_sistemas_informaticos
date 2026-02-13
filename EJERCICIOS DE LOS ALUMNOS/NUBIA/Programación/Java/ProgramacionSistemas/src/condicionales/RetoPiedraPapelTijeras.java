package condicionales;
import java.util.Scanner;
import java.util.Random;


public class RetoPiedraPapelTijeras {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random mano = new Random();
    
        // TÍTULO
        System.out.println("JUEGO PIEDRA, PAPEL O TIJERAS");
        
        //ELECCIONES
        System.out.println("Elige piedra (1), papel (2) o tijeras (3)");
        int manoJugador = sc.nextInt();
        
        int manoMaquina = mano.nextInt(3) + 1;

        // NÚMERO A PALABRA
        String eleccionJugador = "";
        if (manoJugador == 1) { eleccionJugador = "Piedra";
        }
        else if (manoJugador == 2) { eleccionJugador = "Papel";
        }
        else if (manoJugador == 3) { eleccionJugador = "Tijeras";
        }
        else { eleccionJugador = "Opción inválida";
        }

        String eleccionMaquina = "";
        if (manoMaquina == 1) { eleccionMaquina = "Piedra";
        }
        else if (manoMaquina == 2) { eleccionMaquina = "Papel";
        }
        else { eleccionMaquina = "Tijeras";
        }

        // MUESTRA ELECCIONES
        System.out.println("Has elegido: " + eleccionJugador);
        System.out.println("El oponente ha elegido: " + eleccionMaquina);

        // RESULTADOS
        if (manoJugador < 1 || manoJugador > 3) {
            System.out.println("¡Tramposo! Ese número no vale.");
        }
        else if (manoJugador == manoMaquina) {
            System.out.println("¡Empate!");
        } 
        else if ((manoJugador == 1 && manoMaquina == 3) || 
                   (manoJugador == 2 && manoMaquina == 1) || 
                   (manoJugador == 3 && manoMaquina == 2)) {
            System.out.println("HAS GANADO");
        } 
        else {
            System.out.println("Has perdido...");
        }

        sc.close();
    }
}