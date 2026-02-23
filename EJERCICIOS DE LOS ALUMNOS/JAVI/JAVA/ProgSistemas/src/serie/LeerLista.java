package serie;

import java.io.*;
import java.util.ArrayList;

public class LeerLista {

    public static void main(String[] args) {

        try (ObjectInputStream ois =
                     new ObjectInputStream(new FileInputStream("/prueba/personas.dat"))) {

            ArrayList<Persona> lista =
                    (ArrayList<Persona>) ois.readObject();

            for (Persona p : lista) {
                System.out.println(p);
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
