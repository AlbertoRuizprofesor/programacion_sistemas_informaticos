package Ejercicio7;

public class Main {
    public static void main(String[] args) {
        // Construyendo un videojuego con el Builder
        Videojuego miJuego = new VideojuegoBuilder()
                .nombre("The Witcher 3")
                .anio(2015)
                .precio(29.99)
                .plataforma("PC / PS4 / Xbox One")
                .sinopsis("Un cazador de monstruos busca a su hija adoptiva en un mundo abierto.")
                .requerimientosMinimos("Intel i5-2500K, 6GB RAM, GTX 660")
                .build();

        // Mostramos el resultado
        miJuego.mostrarFichaTecnica();
             
    }
}
