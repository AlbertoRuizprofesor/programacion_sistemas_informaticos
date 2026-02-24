package arrayList;
import java.util.ArrayList;

public class Ejercicio7 {
    public static void main(String[] args) {

        var personas = new ArrayList<Persona>();

        personas.add(new Persona("Ana", 25));
        personas.add(new Persona("Luis", 30));
        personas.add(new Persona("Marta", 22));

        for (var p : personas) {
            System.out.println(p);
        }
    }
}


