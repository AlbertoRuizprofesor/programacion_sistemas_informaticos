package poobancos;

public class CuentaBancaria extends Banco {

    private int numeroCuenta;
    private double saldo;

    public CuentaBancaria(String nombre_banco, 
    		int numeroCuenta, double saldoInicial) {
        super(nombre_banco);
        this.numeroCuenta = numeroCuenta;
        this.saldo = saldoInicial;
    }

    public int getNumeroCuenta() {
        return numeroCuenta;
    }

    public void setNumeroCuenta(int numeroCuenta) {
        this.numeroCuenta = numeroCuenta;
    }

    public double getSaldo() {
        return saldo;
    }

    // 1) Ingresar
    public void ingresar(double importe) {
        if (importe <= 0) {
            System.out.println("❌ El importe a ingresar debe ser mayor que 0.");
            return;
        }
        saldo += importe;
        System.out.println("✅ Ingreso realizado: +" + importe);
    }

    // 2) Sacar (retirar)
    public void sacar(double importe) {
        if (importe <= 0) {
            System.out.println("❌ El importe a retirar debe ser mayor que 0.");
            return;
        }
        if (importe > saldo) {
            System.out.println("❌ Saldo insuficiente. Saldo actual: " + saldo);
            return;
        }
        saldo -= importe;
        System.out.println("✅ Retirada realizada: -" + importe);
    }

    // 3) Mostrar saldo
    public void mostrarSaldo() {
        System.out.println("💰 Saldo actual: " + saldo);
    }

    @Override
    public String toString() {
        return "CuentaBancaria [banco=" + getNombre_banco() +
               ", numeroCuenta=" + numeroCuenta +
               ", saldo=" + saldo + "]";
    }
}