package arrayList;
import java.util.ArrayList;

public class Ejercicio2 {
    public static void main(String[] args) {

        var numeros = new ArrayList<Integer>();

        numeros.add(10);
        numeros.add(20);
        numeros.add(30);
        numeros.add(40);
        numeros.add(50);
        numeros.add(60);

        int suma = 0;

        for (var num : numeros) {
            suma += num;
        }

        System.out.println("Suma total: " + suma);
    }
}
