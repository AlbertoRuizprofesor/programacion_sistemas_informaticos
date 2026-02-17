package Ejemplos;

public class Animal {
	
public void hacerSonido() {
        System.out.println("El animal hace un sonido genérico");
    }
}


class Perro extends Animal {
    @Override
    public void hacerSonido() {
        System.out.println("El perro dice: ¡Guau! ¡Guau!");
    }
}
