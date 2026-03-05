package arrayList;
import java.util.ArrayList;

public class Ejercicio1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        var nombres = new ArrayList<String>();

        nombres.add("Ana");
        nombres.add("Luis");
        nombres.add("Marta");
        nombres.add("Pedro");
        nombres.add("Lucía");

        for (var nombre : nombres) {
            System.out.println(nombre);
        }
    }
}

