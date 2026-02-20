package serie;

import java.io.*;
import java.util.ArrayList;

public class GuardarLista {

    public static void main(String[] args) {

        ArrayList<Persona> lista = new ArrayList<>();

        lista.add(new Persona("Ana", 20));
        lista.add(new Persona("Luis", 22));
        lista.add(new Persona("Marta", 19));

        try (ObjectOutputStream oos =
                     new ObjectOutputStream(new FileOutputStream("c:\\prueba\\persona.dat"))) {

            oos.writeObject(lista);

            System.out.println("Lista guardada");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}



