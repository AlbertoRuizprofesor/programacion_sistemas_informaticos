package factory1;

//Ejemplo de uso
public class Main {
	public static void main(String[] args) {
		// Crear una fábrica de electrodomésticos
		Fabrica fabricaElectrodomesticos = new FabricaElectrodomesticos();
		// Utilizar la fábrica para crear un electrodoméstico
		Producto electrodomestico = fabricaElectrodomesticos.crearProducto();
		// Operar con el electrodoméstico
		electrodomestico.venta();

		// Crear una fábrica de ropa
		Fabrica fabricaRopa = new FabricaRopa();
		// Utilizar la fábrica para crear ropa
		Producto ropa = fabricaRopa.crearProducto();
		// Operar con la ropa
		ropa.venta();
		
		// Crear una fábrica de vehiculo
		Fabrica fabricaVehiculo = new FabricaVehiculo();
		// Utilizar la fábrica para crear vehiculo
		Producto vehiculo = fabricaVehiculo.crearProducto();
		// Operar con el vehiculo
		vehiculo.venta();
	}
}


