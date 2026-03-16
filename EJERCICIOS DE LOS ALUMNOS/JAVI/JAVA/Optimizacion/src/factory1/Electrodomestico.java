package factory1;

//Implementación de productos concretos: electrodomésticos
class Electrodomestico implements Producto {
	@Override
	public void venta() {
		System.out.println("venta de electrodoméstico.");
	}
}
