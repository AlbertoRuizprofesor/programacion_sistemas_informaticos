package interface2;

public class Calculadora implements Operaciones {

    public int sumar(int a, int b) {
        return a + b;
    }

    public int restar(int a, int b) {
        return a - b;
    }

    public int multi(int a, int b) {
        return a * b;
    }

    public int divi(int a, int b) {
        return a / b;
    }

    public void mostrar(int a, int b) {
        System.out.println("Suma: " + sumar(a,b));
        System.out.println("Resta: " + restar(a,b));
        System.out.println("Multiplicación: " + multi(a,b));
        System.out.println("División: " + divi(a,b));
    }
}
