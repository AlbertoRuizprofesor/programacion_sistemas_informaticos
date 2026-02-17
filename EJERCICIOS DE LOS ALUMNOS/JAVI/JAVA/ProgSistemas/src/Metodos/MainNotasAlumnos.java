package Metodos;

public class MainNotasAlumnos {

    public static void main(String[] args) {
        // Instanciamos la clase de lógica
        NotasAlumnos gestion = new NotasAlumnos();
        
        // Pedimos los datos al usuario
        double[] notasIngresadas = gestion.pedirNotas();
        
        // Procesamos y mostramos la lista de resultados
        gestion.mostrarResultados(notasIngresadas);
    }
}


