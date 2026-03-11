package Refactorizacion;

import java.util.Scanner;

public class UsuarioNombre {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Llamada a los métodos extraídos
        String nombre = obtenerDato(sc, "Introduce tu nombre: ");
        String usuario = obtenerDato(sc, "Introduce tu usuario: ");
        
        sc.close();
        
        imprimirDatos(nombre, usuario);
    }

    // Método extraído para la entrada de datos
    private static String obtenerDato(Scanner sc, String mensaje) {
        System.out.print(mensaje);
        return sc.nextLine();
    }

    // Método extraído para la salida de datos
    private static void imprimirDatos(String nombre, String usuario) {
        System.out.println("Nombre: " + nombre);
        System.out.println("Usuario: " + usuario);
    }
}

