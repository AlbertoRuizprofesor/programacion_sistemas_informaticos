package factory1;

//Implementación de fábrica para electrodomésticos
class FabricaElectrodomesticos extends Fabrica {
	@Override
	public Producto crearProducto() {
		return new Electrodomestico();
	}
}
