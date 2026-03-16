package factory1;

class FabricaVehiculo extends Fabrica {
    @Override
    public Producto crearProducto() {
        return new Vehiculo();
    }
}


