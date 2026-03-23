package ejercicio5;

public class CuentaBancaria {
    private String titular;
    private double saldo;

    public CuentaBancaria(String titular, double saldoInicial) {
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    // Método para ingresar dinero
    public void ingresar(double cantidad) {
        if (cantidad > 0) {
            this.saldo += cantidad;
            System.out.println("Ingresados: " + cantidad + "€. Nuevo saldo: " + this.saldo + "€.");
        }
    }

    // Método para retirar dinero
    public void retirar(double cantidad) {
        if (cantidad <= saldo) {
            this.saldo -= cantidad;
            System.out.println("Retirados: " + cantidad + "€. Saldo restante: " + this.saldo + "€.");
        } else {
            System.out.println("Error: Saldo insuficiente para retirar " + cantidad + "€.");
        }
    }

    // Método para mostrar el saldo actual
    public void mostrarSaldo() {
        System.out.println("El saldo actual de " + titular + " es: " + saldo + "€.");
    }
}
