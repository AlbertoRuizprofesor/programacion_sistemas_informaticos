package proxy;

public class ProxyDocumento implements Documento {
    private DocumentoReal documentoReal;
    private String nombre;

    public ProxyDocumento(String nombre) {
        this.nombre = nombre;
    }

    @Override
    public void mostrar() {
        if (documentoReal == null) {
            documentoReal = new DocumentoReal(nombre);
        }
        documentoReal.mostrar();
    }
}
