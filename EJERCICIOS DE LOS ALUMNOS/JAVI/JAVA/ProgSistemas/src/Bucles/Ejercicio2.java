//11) Mayor y menor de N números.


import java.util.Scanner;

public class Ejercicio2 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("¿Cuántos números?: ");
    int n = sc.nextInt();

    System.out.print("Introduzca el número 1: ");
    int num1 = sc.nextInt();

    int mayor = num1;
    int menor = num1;
    
    for(int i = 1; i<=n; i++) {
    	System.out.print("Introduzca el número 2: ");
        int num2 = sc.nextInt();
                       	
        if (num2 > mayor) mayor = num2;
        if (num2 < menor) menor = num2;    	
    }
    System.out.println("Mayor: " + mayor);
    System.out.println("Menor: " + menor);   
    
    sc.close();
  }
}
