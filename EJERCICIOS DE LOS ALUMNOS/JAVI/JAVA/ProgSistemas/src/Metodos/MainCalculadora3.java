package Metodos;

import java.util.Scanner;

public class MainCalculadora3 {

    public static void main(String[] args) {
        
        Calculadora3 calculadora = new Calculadora3();
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Introduzca el número 1: ");
        int num1 = teclado.nextInt();
        
        System.out.println("Introduzca el número 2: ");
        int num2 = teclado.nextInt();
        
        // ¡IMPORTANTE!: Asignamos los valores a los atributos del objeto
        calculadora.n1 = num1;
        calculadora.n2 = num2;
        
        // Ahora llamamos al método que imprime todo
        // No hace falta llamar a sumar() o restar() aquí porque mostrarResultado() ya los llama por dentro
        calculadora.mostrarResultado();
        
        teclado.close(); // Buena práctica cerrar el scanner
    }
}
