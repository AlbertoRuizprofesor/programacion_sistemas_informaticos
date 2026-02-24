package arrayList;
import java.util.Collections;
import java.util.Scanner;

public class Ejercicio8 {
    public static void main(String[] args) {

        var notas = new ArrayList<Double>();
        var sc = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            System.out.print("Introduce nota: ");
            notas.add(sc.nextDouble());
        }

        double suma = 0;

        for (var nota : notas) {
            suma += nota;
        }

        System.out.println("Media: " + (suma / notas.size()));
        System.out.println("Mayor: " + Collections.max(notas));
        System.out.println("Menor: " + Collections.min(notas));
    }
}

