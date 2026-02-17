package Arrays;

import java.util.Scanner;

public class Ejemplo {
    
    public double calcularSuma(double[] notas) {
        double suma = 0;
        for (double nota : notas) {
            suma += nota;
        }
        return suma;
    }
    
    public double calcularMedia(double[] notas) {
        if (notas.length == 0) return 0;
        return calcularSuma(notas) / notas.length;
    }
    
    public String estadoAlumno(double media) {
        return (media >= 5) ? "Aprobado" : "Suspenso";
    }

    public void mostrarResultados(double[] notas) {
        double media = calcularMedia(notas);
        String[] metodos = {"Suma Total", "Media Final", "Estado"};
        
        System.out.println("\n--- Resumen de Calificaciones ---");
        System.out.println(metodos[0] + ": " + calcularSuma(notas));
        System.out.println(metodos[1] + ": " + String.format("%.2f", media));
        System.out.println(metodos[2] + ": " + estadoAlumno(media));
    }

      public double[] pedirNotas() {
        Scanner teclado = new Scanner(System.in);
        
        System.out.print("¿Cuántas notas vas a introducir?: ");
        int cantidad = teclado.nextInt();
        
        double[] notas = new double[cantidad];

        for (int i = 0; i < notas.length; i++) {
            System.out.print("Introduce la nota " + (i + 1) + ": ");
            notas[i] = teclado.nextDouble();
        }

        return notas;
    }
}