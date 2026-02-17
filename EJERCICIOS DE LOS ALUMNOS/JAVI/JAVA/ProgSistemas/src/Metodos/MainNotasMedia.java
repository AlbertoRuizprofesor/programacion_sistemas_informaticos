package Metodos;

import java.util.Scanner;

public class MainNotasMedia {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        
        NotasMedia calificacion = new NotasMedia();
        
        
        System.out.println("Introduzca la nota 1: ");
        calificacion.numero1 = teclado.nextDouble(); 
        
        System.out.println("Introduzca la nota 2: ");
        calificacion.numero2 = teclado.nextDouble();
        
        System.out.println("Introduzca la nota 3: ");
        calificacion.numero3 = teclado.nextDouble();
        
      
        calificacion.resultados();
        
        teclado.close();
    }
}