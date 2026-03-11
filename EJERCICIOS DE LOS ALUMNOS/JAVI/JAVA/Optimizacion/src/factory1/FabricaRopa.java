package factory1;

class FabricaRopa extends Fabrica {
    @Override
    public Producto crearProducto() {
        return new Ropa();
    }
}