package buclesObligatorios;
import java.util.Scanner;


public class Menu {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c = new Scanner(System.in);

        boolean codigo = false;
        int opcion;

        while (!codigo) {

            System.out.print("Dime la opcion 1 (sumar) 2 (restar) 3 (Salir): ");
            opcion = c.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println("Has elegido sumar");
                    break;

                case 2:
                    System.out.println("Has elegido restar");
                    break;

                case 3:
                    System.out.println("Has elegido salir");
                    codigo = true;
                    break;

                default:
                    System.out.println("Error");
            }
        }

        c.close();

	}

}
