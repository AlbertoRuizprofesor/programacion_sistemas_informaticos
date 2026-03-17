package composite;

public class Archivo implements Componente {
    private String nombre;

    public Archivo(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public void mostrar() {
        System.out.println("Archivo: " + nombre);
    }
}
