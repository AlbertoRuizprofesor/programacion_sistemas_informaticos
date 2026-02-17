Lee un número 1–7 y muestra el día. Si no, error.
import java.util.Scanner;
 
public class Ej15DiaSemana {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Día (1-7): ");
    int d = sc.nextInt();
 
    String nombre = switch (d) {
      case 1 -> "Lunes";
      case 2 -> "Martes";
      case 3 -> "Miércoles";
      case 4 -> "Jueves";
      case 5 -> "Viernes";
      case 6 -> "Sábado";
      case 7 -> "Domingo";
      default -> null;
    };
 
    if (nombre == null)
System.out.println("ERROR: día inválido");
    else System.out.println(nombre);
 
    sc.close();
  }
}

Dime la estructura del switch case