package Metodos;

public class Calculadora3 {
    // Atributos de la clase
    public int n1;
    public int n2;

    // Métodos que operan con los atributos del objeto
    public int sumar() {
        return n1 + n2;
    }

    public int restar() {
        return n1 - n2;
    }

    public int multiplicar() {
        return n1 * n2;
    }

    public int dividir() {
        // Validación para evitar división por cero
        if (n1 == 0 || n2 == 0) return 0; 
        return (n1 > n2) ? n1 / n2 : n2 / n1;
    }
    
 // Opción A: Un método para cada atributo
    public double raizDeN1() {
        return Math.sqrt(n1);
    }

    public double raizDeN2() {
        return Math.sqrt(n2);
    }
	

    public void mostrarResultado() {
        System.out.println("La suma es: " + sumar());
        System.out.println("La resta es: " + restar());
        System.out.println("La multiplicación es: " + multiplicar());
        System.out.println("La división es: " + dividir());
        System.out.println("La raíz de número 1 es: " + raizDeN1());
        System.out.println("La raíz de número 2 es: " + raizDeN2());
    }
}