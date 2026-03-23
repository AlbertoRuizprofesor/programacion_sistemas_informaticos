package ejercicio5;

public class Main {
    public static void main(String[] args) {
        // Creamos una cuenta con un saldo inicial de 500
        CuentaBancaria miCuenta = new CuentaBancaria("Juan Pérez", 500.0);

        // Realizamos operaciones
        miCuenta.mostrarSaldo();    // Consultar saldo inicial
        miCuenta.ingresar(200.0);   // Ingresar dinero
        miCuenta.retirar(100.0);    // Retirar dinero
        miCuenta.retirar(1000.0);   // Intentar retirar más de lo que hay
        miCuenta.mostrarSaldo();    // Ver resultado final
    }
}