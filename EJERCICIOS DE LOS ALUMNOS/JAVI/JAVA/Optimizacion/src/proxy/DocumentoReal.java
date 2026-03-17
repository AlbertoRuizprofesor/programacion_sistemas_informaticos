package proxy;

public class DocumentoReal implements Documento {
    private String nombre;

    public DocumentoReal(String nombre) {
        this.nombre = nombre;
        cargarDesdeDisco(nombre);
    }

    private void cargarDesdeDisco(String nombre) {
        System.out.println("Cargando " + nombre);
    }

    @Override
    public void mostrar() {
        System.out.println("Mostrando " + nombre);
    }
}
