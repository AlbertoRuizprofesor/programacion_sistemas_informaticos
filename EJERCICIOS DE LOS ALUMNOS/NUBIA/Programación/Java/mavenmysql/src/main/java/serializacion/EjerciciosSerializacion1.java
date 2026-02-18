package serializacion;

import java.io.*;

class Persona implements Serializable {
	
	private String nombre;
	private int edad;
	
	public Persona(String nombre, int edad) {
		this.nombre=nombre;
		this.edad=edad;
	}
	
	public String toString() {
		return "Persona: "+nombre+"\nEdad: "+edad;
	}

}

public class EjerciciosSerializacion1 {
	public static void main(String[] args) {
		
		// crear objeto "persona"
		Persona persona=new Persona("Darío", 17);
		
		// Serializar (salida) objeto
		try {
			FileOutputStream archivoSalida=new FileOutputStream("c:\\prueba\\persona.ser");
			ObjectOutputStream objetoSalida=new ObjectOutputStream(archivoSalida);
			
			objetoSalida.writeObject(persona);
			objetoSalida.close();
			archivoSalida.close();
			
			System.out.println("Objeto serializado correctamente");
		}
		
		catch (IOException e) {
			e.printStackTrace();
		}
		
		// Deserializar el objeto
		try {
			FileInputStream archivoEntrada=new FileInputStream("c:\\prueba\\persona.ser");
			ObjectInputStream objetoEntrada=new ObjectInputStream(archivoEntrada);
			Persona personaDeserializada =(Persona) objetoEntrada.readObject();
			objetoEntrada.close();
			archivoEntrada.close();
			System.out.println("Objeto deserializado correctamente");
			System.out.println(personaDeserializada);
		}
		
		catch (IOException | ClassNotFoundException e) {
			e.printStackTrace();
		}
	}
}
	

	
