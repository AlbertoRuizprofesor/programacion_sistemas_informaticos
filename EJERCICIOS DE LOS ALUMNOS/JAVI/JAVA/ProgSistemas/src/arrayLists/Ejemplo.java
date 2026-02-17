package arrayLists;

import java.util.ArrayList;
import java.util.Collections; // Librería extra muy útil

public class Ejemplo {

    public static void main(String[] args) {
        
        ArrayList<String> nombres = new ArrayList<>();

        // 1. AÑADIR (Create)
        nombres.add("Anabel");
        nombres.add("Francisco");
        nombres.add("Pedro");
        nombres.add("Marta");

        // 2. CONSULTAR ELEMENTOS (Read)
        // Obtener uno específico por índice
        String primera = nombres.get(0); 
        System.out.println("La primera persona es: " + primera);

        // Saber si alguien está en la lista (devuelve true/false)
        boolean estaFrancisco = nombres.contains("Francisco");
        System.out.println("¿Está Francisco en la lista? " + estaFrancisco);

        // Saber en qué posición está alguien
        int posicionMarta = nombres.indexOf("Marta");
        System.out.println("Marta está en el índice: " + posicionMarta);

        // 3. EDITAR / REEMPLAZAR (Update)
        // Queremos cambiar a "Pedro" por "Pepe" (Pedro está en el índice 2)
        nombres.set(2, "Pepe"); 
        System.out.println("Lista tras editar a Pedro: " + nombres);

        // 4. ORDENAR (Extra útil)
        // Ordena la lista alfabéticamente
        Collections.sort(nombres);
        System.out.println("Lista ordenada: " + nombres);

        // 5. BORRAR (Delete)
        // Por índice
        nombres.remove(0); 
        // Por objeto exacto
        nombres.remove("Anabel");
        // Borrar todo el contenido
        // nombres.clear(); 

        // 6. RECORRER CON INFORMACIÓN EXTRA
        System.out.println("\n--- Resumen Final ---");
        if (nombres.isEmpty()) {
            System.out.println("La lista está vacía.");
        } else {
            for (int i = 0; i < nombres.size(); i++) {
                System.out.println("Posición " + i + ": " + nombres.get(i));
            }
        }
    }
}