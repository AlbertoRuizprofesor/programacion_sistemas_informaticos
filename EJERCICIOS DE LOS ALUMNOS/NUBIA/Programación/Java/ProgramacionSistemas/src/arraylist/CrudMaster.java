package arraylist;
import java.util.ArrayList;
import java.util.Scanner;

public class CrudMaster {
    static Scanner sc = new Scanner(System.in);
    static ArrayList<String> clientes = new ArrayList<>();

    public static void main(String[] args) {
        int opcion = 0;

        // OPCIONES MENÚ
        while (opcion != 6) {
            mostrarMenu();
            opcion = sc.nextInt();
            sc.nextLine(); 

   
            if (opcion == 1) {
                añadirCliente();
            } else if (opcion == 2) {
                eliminarCliente();
            } else if (opcion == 3) {
                modificarCliente();
            } else if (opcion == 4) {
                buscarCliente();
            } else if (opcion == 5) {
                listarClientes();
            } else if (opcion == 6) {
                System.out.println("Saliendo del sistema...");
            } else {
                System.out.println("Opción no válida, intenta de nuevo.");
            }
        }
    }

    // MENÚ A MOSTRAR

    public static void mostrarMenu() {
        System.out.println("\n GESTIÓN DE CLIENTES");
        System.out.println("1. Añadir");
        System.out.println("2. Eliminar");
        System.out.println("3. Modificar");
        System.out.println("4. Buscar");
        System.out.println("5. Listar");
        System.out.println("6. Salir");
        System.out.print("Seleccione: ");
    }

    public static void añadirCliente() {
        System.out.print("Nombre del nuevo cliente: ");
        clientes.add(sc.nextLine());
        System.out.println("¡Cliente guardado!");
    }

    public static void eliminarCliente() {
        System.out.print("Nombre a eliminar: ");
        String nombre = sc.nextLine();
        if (clientes.remove(nombre)) {
            System.out.println("Eliminado correctamente.");
        } else {
            System.out.println("No se encontró ese nombre.");
        }
    }

    public static void modificarCliente() {
        System.out.print("Nombre actual: ");
        String actual = sc.nextLine();
        int indice = clientes.indexOf(actual);
        
        if (indice != -1) {
            System.out.print("Nuevo nombre: ");
            clientes.set(indice, sc.nextLine());
            System.out.println("Modificado con éxito.");
        } else {
            System.out.println("El cliente no existe.");
        }
    }

    public static void buscarCliente() {
        System.out.print("Nombre a buscar: ");
        String nombre = sc.nextLine();
        if (clientes.contains(nombre)) {
            System.out.println("El cliente está en la lista.");
        } else {
            System.out.println("No se ha encontrado.");
        }
    }

    public static void listarClientes() {
        if (clientes.isEmpty()) {
            System.out.println("No hay clientes registrados.");
        } else {
            System.out.println("Listado:");
            for (String c : clientes) {
                System.out.println("- " + c);
            }
        }
    }
}