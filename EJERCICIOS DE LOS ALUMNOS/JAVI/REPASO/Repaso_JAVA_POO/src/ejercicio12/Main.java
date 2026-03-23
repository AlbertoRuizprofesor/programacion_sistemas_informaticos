package ejercicio12;

public class Main {
    public static void main(String[] args) {
        
        // Creamos el objeto inicial
        Videojuego miJuego = new Videojuego("The Legend of Zelda", "Nintendo Switch", 50);
        
        // Mostramos estado inicial
        miJuego.mostrarInformacion();
        
        // Simulamos una sesión de juego de 5 horas
        miJuego.jugar(5);
        
        // Simulamos otra sesión de 3 horas
        miJuego.jugar(3);
        
        // Mostramos la información actualizada
        miJuego.mostrarInformacion();
    }
}