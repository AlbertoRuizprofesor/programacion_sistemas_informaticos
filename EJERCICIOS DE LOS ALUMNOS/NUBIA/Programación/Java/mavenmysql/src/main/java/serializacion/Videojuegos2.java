package serializacion;

import java.io.*;
import java.util.ArrayList; 

class Videojuego2 implements Serializable {
	
	private int codigo;
	private String nombre;
	private double precio;
	
	public Videojuego2(int codigo, String nombre, double precio) {
		this.codigo = codigo;
		this.nombre = nombre;
		this.precio = precio;
	}
	
	public String toString() {
		return "\nVideojuego: " + nombre + "\nCódigo: " + codigo + "\nPrecio: " + precio;
	}
}

public class Videojuegos2 {
	public static void main(String[] args) {
		
		// 1. Creamos el ArrayList y añadimos varios objetos Videojuego
		ArrayList<Videojuego2> listaJuegos = new ArrayList<Videojuego2>();
		
		listaJuegos.add(new Videojuego2(1, "Hollow Knight", 20));
		listaJuegos.add(new Videojuego2(2, "Elden Ring", 60));
		listaJuegos.add(new Videojuego2(3, "Stardew Valley", 15));
		
		// --- SERIALIZAR (Salida de la lista completa) ---
		try {
			FileOutputStream archivoSalida = new FileOutputStream("c:\\prueba\\videojuego.ser");
			ObjectOutputStream objetoSalida = new ObjectOutputStream(archivoSalida);
			
			// Guardamos toda la lista de una sola vez
			objetoSalida.writeObject(listaJuegos);
			
			objetoSalida.close();
			archivoSalida.close();
			
			System.out.println("Lista de objetos serializada correctamente");
		}
		catch (IOException e) {
			e.printStackTrace();
		}
		
		// --- DESERIALIZAR (Entrada de la lista completa) ---
		try {
			FileInputStream archivoEntrada = new FileInputStream("c:\\prueba\\videojuego.ser");
			ObjectInputStream objetoEntrada = new ObjectInputStream(archivoEntrada);
			
			// Leemos el objeto y le decimos que es un ArrayList de Videojuegos
			ArrayList<Videojuego2> listaFinal = (ArrayList<Videojuego2>) objetoEntrada.readObject();
			
			objetoEntrada.close();
			archivoEntrada.close();
			
			System.out.println("Lista deserializada correctamente. Contenido:");
			
			System.out.println(listaFinal);
			
		}
		catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}
