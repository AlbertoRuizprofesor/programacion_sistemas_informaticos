package arrayList;

import java.util.ArrayList;
import java.util.Collections;

public class Ejercicio6 {
    public static void main(String[] args) {

        var numeros = new ArrayList<Integer>();

        numeros.add(25);
        numeros.add(10);
        numeros.add(40);
        numeros.add(5);

        System.out.println("Mayor: " + Collections.max(numeros));
        System.out.println("Menor: " + Collections.min(numeros));
    }
}

