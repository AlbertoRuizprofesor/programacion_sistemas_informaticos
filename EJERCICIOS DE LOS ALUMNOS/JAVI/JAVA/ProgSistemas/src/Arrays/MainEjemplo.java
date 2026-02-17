package Arrays;

public class MainEjemplo {

    public static void main(String[] args) {
        
        Ejemplo gestion = new Ejemplo();        
        
        double[] notasIngresadas = gestion.pedirNotas();        
        
        gestion.mostrarResultados(notasIngresadas);
    }
}