package serializacion;

import java.io.*;

class Videojuego implements Serializable {
	
	private int codigo;
	private String nombre;
	private double precio;
	
	public Videojuego(int codigo, String nombre, double precio) {
		this.codigo=codigo;
		this.nombre=nombre;
		this.precio=precio;
	}
	
	public String toString() {
		return "Videojuego: "+nombre+"\nCódigo: "+codigo+"\nPrecio: "+precio;
	}

}

public class Videojuegos {
	public static void main(String[] args) {
		
		// crear objeto "juego"
		Videojuego videojuego=new Videojuego(1, "Hollow Knight", 20);
		
		// Serializar (salida) objeto
		try {
			FileOutputStream archivoSalida=new FileOutputStream("c:\\prueba\\videojuego.ser");
			ObjectOutputStream objetoSalida=new ObjectOutputStream(archivoSalida);
			
			objetoSalida.writeObject(videojuego);
			objetoSalida.close();
			archivoSalida.close();
			
			System.out.println("Objeto serializado correctamente");
		}
		
		catch (IOException e) {
			e.printStackTrace();
		}
		
		// Deserializar el objeto
		try {
			FileInputStream archivoEntrada=new FileInputStream("c:\\prueba\\videojuego.ser");
			ObjectInputStream objetoEntrada=new ObjectInputStream(archivoEntrada);
			Videojuego videojuegoDeserializado =(Videojuego) objetoEntrada.readObject();
			objetoEntrada.close();
			archivoEntrada.close();
			System.out.println("Objeto deserializado correctamente");
			System.out.println(videojuegoDeserializado);
		}
		
		catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}
	

	
