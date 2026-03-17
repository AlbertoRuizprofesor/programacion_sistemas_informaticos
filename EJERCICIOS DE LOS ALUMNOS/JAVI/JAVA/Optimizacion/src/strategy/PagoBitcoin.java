package strategy;

//Nueva Estrategia: Pago con Bitcoins
class PagoBitcoin implements EstrategiaPago {
 private String direccionBilletera; // Dirección alfanumérica (Wallet)

 public PagoBitcoin(String direccionBilletera) {
     this.direccionBilletera = direccionBilletera;
 }

 @Override
 public void pagar(double cantidad) {
     // En una app real, aquí iría la conexión a la Blockchain
     System.out.println("Pagando " + cantidad + " € (convertidos a BTC) usando la Wallet: " + direccionBilletera);
 }
}