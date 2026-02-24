package primerospasos;

import java.util.ArrayList;
import java.util.Scanner;

public class CRUDswitchcase {

    public static void main(String[] args) {
    	Scanner sc = new Scanner(System.in);
        ArrayList<String> lista = new ArrayList<>();
        int opcion;
        
        do {
        	System.out.println("----- CRUD -----");
            System.out.println("1. añadir");
            System.out.println("2. eliminar");
            System.out.println("3. modificar");
            System.out.println("4. buscar");
            System.out.println("5. listado");
            System.out.println("6. Salir");
            System.out.print("que quieres hacer: ");

            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer
            
            //ArrayList<String> nombre = new ArrayList<>();
            
            switch (opcion) {

            case 1:            	
            	System.out.print("nombre?: ");
                String añadir=sc.next();
                lista.add(añadir);
                System.out.println("nombre guardado.");
                break;
            case 2:
            	System.out.print("cual elimino?: ");
            	String eliminar=sc.next();
            	lista.remove(eliminar);
                System.out.println("nombre eliminado.");
                break;
            case 3:
            	System.out.print("cual modifico?: ");
            	String elimino=sc.next();
            	if (lista.contains(elimino)) {
                    System.out.println("Encontrado en la posicion: " + lista.indexOf(elimino));
                    lista.remove(elimino);
                } else {
                    System.out.println("No encontrado.");
                    break;
                }
            	lista.remove(elimino);
            	System.out.print("cual añado?: ");
            	String añado=sc.next();
            	lista.add(añado);
            	System.out.println("modificado: ");
                break;
            case 4:
            	System.out.print("Introduce elemento a buscar: ");
                String buscar = sc.nextLine();
                if (lista.contains(buscar)) {
                    System.out.println("Encontrado en la posicion: " + lista.indexOf(buscar));
                } else {
                    System.out.println("No encontrado.");
                    break;
                }
                break;
            	
            case 5:
            	System.out.println("listado "+lista);
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