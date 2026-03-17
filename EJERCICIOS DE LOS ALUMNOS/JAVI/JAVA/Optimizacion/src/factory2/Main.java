package factory2;

//Ejemplo de uso
public class Main {
	public static void main(String[] args) {
		// Crear una fábrica de electrodomésticos
		Fabrica fabricaProfesores = new FabricaProfesores();
		// Utilizar la fábrica para crear un electrodoméstico
		Persona profesor = fabricaProfesores.crearPersona();
		// Operar con el electrodoméstico
		profesor.accion();

		// Crear una fábrica de electrodomésticos
		Fabrica fabricaAlumno = new FabricaAlumno();
		// Utilizar la fábrica para crear un electrodoméstico
		Persona alumno = fabricaAlumno.crearPersona();
		// Operar con el electrodoméstico
		alumno.accion();

	}
}
