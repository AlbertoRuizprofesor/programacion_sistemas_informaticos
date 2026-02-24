package arrayList;

import java.util.ArrayList;

public class Ejercicio3 {
    public static void main(String[] args) {

        var colores = new ArrayList<String>();

        colores.add("Rojo");
        colores.add("Verde");
        colores.add("Azul");
        colores.add("Amarillo");
        colores.add("Negro");

        colores.remove("Azul");

        System.out.println(colores);
    }
}
