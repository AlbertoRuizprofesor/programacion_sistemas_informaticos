package serie;

import java.io.*;

//Clase que implementa Serializable
class Videojuegos implements Serializable {

	private String nombre;
	private int codigo;
	private String precio;

	public Videojuegos(String nombre, int codigo, String precio) {
		this.nombre = nombre;
		this.codigo = codigo;
		this.precio = precio;		
	}

	public String toString() {
		return "Videojuego: " + nombre + ", codigo : " + codigo + ", precio: " + precio;
	}
}

public class EjercicioSerializado2 {
	public static void main(String[] args) {
		// Crear un objeto Persona
		Videojuegos videojuego = new Videojuegos("WOW", 30, "54");
		// Serializar el objeto
		try {

			FileOutputStream archivoSalida = new FileOutputStream("c:\\prueba\\videojuegosjor.ser");
			ObjectOutputStream objetoSalida = new ObjectOutputStream(archivoSalida);

			objetoSalida.writeObject(videojuego);
			objetoSalida.close();
			archivoSalida.close();

			System.out.println("Objeto serializado correctamente.");

		} catch (IOException e) {
			e.printStackTrace();
		}
		// Deserializar el objeto
		try {

			FileInputStream archivoEntrada = new FileInputStream("c:\\prueba\\videojuegosjor.ser");
			ObjectInputStream objetoEntrada = new ObjectInputStream(archivoEntrada);
			Videojuegos videojuegoDeserializado= (Videojuegos) objetoEntrada.readObject();
			objetoEntrada.close();
			archivoEntrada.close();
			System.out.println("Objeto deserializado correctamente.");
			System.out.println(videojuegoDeserializado);

		} catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}

