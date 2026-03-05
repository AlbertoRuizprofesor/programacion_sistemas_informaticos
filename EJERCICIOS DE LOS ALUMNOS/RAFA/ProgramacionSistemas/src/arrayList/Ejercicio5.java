package arrayList;

import java.util.ArrayList;
import java.util.Collections;

public class Ejercicio5 {
    public static void main(String[] args) {

        var numeros = new ArrayList<Integer>();

        numeros.add(8);
        numeros.add(3);
        numeros.add(15);
        numeros.add(1);
        numeros.add(9);

        Collections.sort(numeros);

        System.out.println("Ordenados: " + numeros);
    }
}
