package ejercicio19;

public class Instituto {
	private String nombreInstituto;
	private Profesor profesorAsignado; // Atributo que es un OBJETO de otra clase

	public Instituto(String nombreInstituto, Profesor profesor) {
		this.nombreInstituto = nombreInstituto;
		this.profesorAsignado = profesor;
	}

	public void mostrarInfoCompleta() {
		System.out.println("INSTITUTO: " + nombreInstituto);
		// Llamamos al método del objeto profesor que tenemos guardado
		System.out.println("Responsable: " + profesorAsignado.obtenerDatos());
	}
}