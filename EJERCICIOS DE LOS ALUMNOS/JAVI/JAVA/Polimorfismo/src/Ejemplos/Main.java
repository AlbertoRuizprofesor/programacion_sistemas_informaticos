package Ejemplos;


public class Main {
	    public static void main(String[] args) {
	        
	        // Polimorfismo en acción:
	        // Declaramos variables de tipo Animal, pero instanciamos objetos específicos
	        Animal miMascota1 = new Perro();
	        Animal miMascota2 = new Gato();

	        System.out.println("Probando sonidos:");
	        
	        // Ambos usan el mismo método, pero el resultado es distinto
	        miMascota1.hacerSonido(); // Imprime: ¡Guau! ¡Guau!
	        miMascota2.hacerSonido(); // Imprime: ¡Miau!
	        
	        System.out.println("---");

	        // También funciona con arrays o listas
	        Animal[] zoologico = { new Perro(), new Gato(), new Animal() };

	        for (Animal a : zoologico) {
	            a.hacerSonido(); 
	            // Java decide en "tiempo de ejecución" qué método llamar
	        }
	    }
	}
	
	


