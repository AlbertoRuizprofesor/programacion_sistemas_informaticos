package arrayList;

import java.util.ArrayList;
import java.util.Scanner;

public class Ejercicio4 {
    public static void main(String[] args) {

        var nombres = new ArrayList<String>();
        var sc = new Scanner(System.in);

        nombres.add("Ana");
        nombres.add("Luis");
        nombres.add("Marta");

        System.out.print("Introduce un nombre: ");
        var buscar = sc.nextLine();

        if (nombres.contains(buscar)) {
            System.out.println("El nombre está en la lista.");
        } else {
            System.out.println("No se encuentra en la lista.");
        }
    }
}
