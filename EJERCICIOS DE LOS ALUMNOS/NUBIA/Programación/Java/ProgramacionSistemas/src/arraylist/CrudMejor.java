package arraylist;
import java.util.ArrayList;
import java.util.Scanner;

public class CrudMejor {

    public static void main(String[] args) {
        ArrayList<String> clientes = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
		
        // 1. Añadir con Scanner
        añadirClientesConScanner(clientes, sc);
	    
        // 2. Eliminar
        System.out.println("\nEscribe el nombre del cliente a eliminar:");
        String borrar = sc.nextLine();
        eliminarCliente(clientes, borrar);

        // --- CAMBIO AQUÍ: Mostrar lista antes de modificar
        System.out.println("\nEstado actual de la lista para modificar:");
        buscarYListar(clientes); 

        // 3. Modificar
        System.out.println("\nIntroduce el índice (número) del cliente que quieres cambiar:");
        int idx = sc.nextInt();
        sc.nextLine();
        
        System.out.println("Introduce el nuevo nombre:");
        String nuevoNom = sc.nextLine();
        modificarCliente(clientes, idx, nuevoNom);

        // 4. Listar resultados finales
        buscarYListar(clientes);
        
        sc.close();
    }

    public static void añadirClientesConScanner(ArrayList<String> lista, Scanner sc) {
        System.out.println("¿Cuántos clientes quieres añadir?");
        int cantidad = sc.nextInt();
        sc.nextLine(); // Limpiar buffer

        for (int i = 0; i < cantidad; i++) {
            System.out.print("Introduce el nombre del cliente " + (i + 1) + ": ");
            String nombre = sc.nextLine();
            lista.add(nombre);
        }
    }

    public static void eliminarCliente(ArrayList<String> lista, String nombre) {
        if (lista.remove(nombre)) {
            System.out.println("Cliente " + nombre + " eliminado.");
        } else {
            System.out.println("El cliente " + nombre + " no existe.");
        }
    }

    public static void modificarCliente(ArrayList<String> lista, int indice, String nuevoNombre) {
        if (indice >= 0 && indice < lista.size()) {
            lista.set(indice, nuevoNombre);
            System.out.println("¡Modificado con éxito!");
        } else {
            System.out.println("Error: El índice " + indice + " no es válido.");
        }
    }

    public static void buscarYListar(ArrayList<String> lista) {
        System.out.println("--- Listado de Clientes ---");
        // Usamos un for normal para mostrar el índice al usuario
        for (int i = 0; i < lista.size(); i++) {
            System.out.println("Índice [" + i + "]: " + lista.get(i));
        }
        System.out.println("Total: " + lista.size());
    }
}