package composite;

public class Main {
    public static void main(String[] args) {
        Archivo archivo1 = new Archivo("archivo1.txt");
        Archivo archivo2 = new Archivo("archivo2.txt");

        Directorio directorio = new Directorio("mi_directorio");
        directorio.agregar(archivo1);
        directorio.agregar(archivo2);

        directorio.mostrar();
    }
}
