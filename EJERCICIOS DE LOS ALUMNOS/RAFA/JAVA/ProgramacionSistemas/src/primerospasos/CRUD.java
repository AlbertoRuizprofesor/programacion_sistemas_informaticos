package primerospasos;

import java.util.ArrayList;
import java.util.Scanner;

public class CRUD {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        ArrayList<String> lista = new ArrayList<>();
        int opcion;

        do {
            System.out.println("\n----- MENU -----");
            System.out.println("1. Agregar elemento");
            System.out.println("2. Mostrar elementos");
            System.out.println("3. Buscar elemento");
            System.out.println("4. Eliminar elemento");
            System.out.println("5. Contar elementos");
            System.out.println("6. Salir");
            System.out.print("Elige una opcion: ");

            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer

            switch (opcion) {

                case 1:
                    System.out.print("Introduce elemento: ");
                    String elemento = sc.nextLine();
                    lista.add(elemento);
                    System.out.println("Elemento agregado.");
                    break;

                case 2:
                    System.out.println("Lista: " + lista);
                    break;

                case 3:
                    System.out.print("Introduce elemento a buscar: ");
                    String buscar = sc.nextLine();
                    if (lista.contains(buscar)) {
                        System.out.println("Encontrado en la posicion: " + lista.indexOf(buscar));
                    } else {
                        System.out.println("No encontrado.");
                    }
                    break;

                case 4:
                    System.out.print("Introduce elemento a eliminar: ");
                    String eliminar = sc.nextLine();
                    if (lista.remove(eliminar)) {
                        System.out.println("Elemento eliminado.");
                    } else {
                        System.out.println("No existe en la lista.");
                    }
                    break;

                case 5:
                    System.out.println("Total elementos: " + lista.size());
                    break;

                case 6:
                    System.out.println("Saliendo del programa...");
                    break;

                default:
                    System.out.println("Opcion no valida.");
            }

        } while (opcion != 6);

        sc.close();
    }
}
