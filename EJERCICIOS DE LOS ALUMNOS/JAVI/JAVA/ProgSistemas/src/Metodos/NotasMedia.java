package Metodos;

import java.util.Scanner;

public class NotasMedia {
    
    public double numero1;
    public double numero2;
    public double numero3;
    
    
    public double calcularMedia() {
    	
    	double media = (numero1 + numero2 + numero3) / 3;
    	
        return media;       
    }
    
    
    public void pedirDatos() {
    	 Scanner teclado = new Scanner(System.in);
    	 int[] notas = new double[6];
    	 for (int i = 0; i < notas.length; i++) {
 			System.out.print("Dime el numero " + (i + 1) + " : ");
 			notas[i] = teclado.nextDouble();
    }
    	 teclado.close();
 		return notas;
    
   
    public void resultados() {
        System.out.println("La nota media es: " + calcularMedia());
    }
}