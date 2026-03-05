package colecciones;

import java.util.ArrayList;
import java.util.Scanner;

public class EjercicioCrud {
	
	static Scanner sc = new Scanner(System.in);//GLOBAL
    static ArrayList<String> lista = new ArrayList<>();//GLOBAL

    public static void main(String[] args) {
    	
        int opcion;
        
        do {
        	System.out.println("----- CRUD -----");
        	System.out.println("0.crear la lista");
            System.out.println("1. añadir");
            System.out.println("2. eliminar");
            System.out.println("3. modificar");
            System.out.println("4. buscar");
            System.out.println("5. listado");
            System.out.println("6. Salir");
            System.out.print("que quieres hacer: ");

            opcion = sc.nextInt();
            sc.nextLine(); // limpiar buffer
            
            
            
            switch (opcion) {
            case 0:
            	crearLista();
            	break;
            case 1:            	
            	agregar();
                break;
            case 2:
            	eliminar();
                break;
            case 3:
            	modificar();
                break;
            case 4:
            	buscar();
                break;
            	
            case 5:
            	listado();
            	break;
            case 6:
            	System.out.println("Saliendo del programa...");
            	System.out.println("cerrado");

                break;
            default:
                System.out.println("Opcion no valida.");
            }
        } while (opcion != 6);

        sc.close();
    }
    public static void crearLista () {
    	lista.add("minerva");
    	lista.add("diana");
    	lista.add("rafa");
    	
    }
    public static void agregar() {
        System.out.print("Nombre?: ");
        String añadir = sc.nextLine();
        lista.add(añadir);
        System.out.println("Nombre guardado.");
    }
    public static void eliminar() {
    	System.out.print("cual elimino?: ");
    	String elimino=sc.next();
        
        if (lista.remove(elimino)) {
            System.out.println("Encontrado en la posicion: " + lista.indexOf(elimino));
            lista.remove(elimino);
            System.out.println("nombre eliminado.");
        } else {
            System.out.println("No encontrado.");
        } 
    }
    public static void modificar() {
    	System.out.print("cual modifico?: ");
    	String elimino=sc.next();
    	if (lista.contains(elimino)) {
            System.out.println("Encontrado en la posicion: " + lista.indexOf(elimino));
            lista.remove(elimino);
        } else {
            System.out.println("No encontrado.");
        }
    	lista.remove(elimino);
    	System.out.print("cual añado?: ");
    	String añado=sc.next();
    	lista.add(añado);
    	System.out.println("modificado: ");
    }
    public static void buscar() {
    	System.out.print("Introduce elemento a buscar: ");
        String buscar = sc.nextLine();
        if (lista.contains(buscar)) {
            System.out.println("Encontrado en la posicion: " + lista.indexOf(buscar));
        } else {
            System.out.println("No encontrado.");
        }
    }
    public static void listado() {
    	System.out.println("listado "+lista);
    }
}














