package prototype;

//Clase Client que utiliza el Prototype
public class MainOrdenador {
	public static void main(String[] args) {
		// Crear un prototipo de ordenador de sobremesa
		OrdenadorSobremesa ordenadorSobremesaPrototipo = new OrdenadorSobremesa("Intel i5", 8, 512, "MSI");

		// Clonar el ordenador de sobremesa prototipo para crear un nuevo ordenador
		OrdenadorSobremesa nuevoOrdenador1 = ordenadorSobremesaPrototipo.clonar();
		System.out.println("Primer ordenador clonado:");
		nuevoOrdenador1.especificaciones();

		// Clonar el ordenador de sobremesa prototipo para crear otro ordenador nuevo
		OrdenadorSobremesa nuevoOrdenador2 = ordenadorSobremesaPrototipo.clonar();
		System.out.println("\nSegundo ordenador clonado:");
		nuevoOrdenador2.especificaciones();

		// Modificar las especificaciones del segundo ordenador clonado
		nuevoOrdenador2.setAlmacenamiento(1024);
		System.out.println("\nSegundo ordenador clonado modificado:");
		nuevoOrdenador2.especificaciones();
		
		// Clonar el ordenador de sobremesa prototipo para crear otro ordenador nuevo
		OrdenadorSobremesa nuevoOrdenador3 = ordenadorSobremesaPrototipo.clonar();
		System.out.println("\nTercer ordenador clonado:");
		nuevoOrdenador3.especificaciones();

		// Modificar las especificaciones del segundo ordenador clonado
		nuevoOrdenador3.setRam(32);
		nuevoOrdenador3.setPlaca("GigaByte");
		nuevoOrdenador3.setAlmacenamiento(2048);
		System.out.println("\nTercer ordenador clonado modificado:");
		nuevoOrdenador3.especificaciones();
	}
}
