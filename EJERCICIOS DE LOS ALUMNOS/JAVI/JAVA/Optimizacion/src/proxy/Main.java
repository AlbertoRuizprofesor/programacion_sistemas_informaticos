package proxy;

public class Main {
    public static void main(String[] args) {
        Documento documento = new ProxyDocumento("documento.pdf");

        // El documento se carga y muestra en el primer acceso
        documento.mostrar();

        // El documento se muestra sin cargar nuevamente en el segundo acceso
        documento.mostrar();
    }
}
