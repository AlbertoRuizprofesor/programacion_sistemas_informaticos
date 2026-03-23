package ejercicio17;

public class Cliente {
	private String nombre;
	private String email;

	public Cliente(String nombre, String email) {
		this.nombre = nombre;
		this.email = email;
	}

	public void mostrarCliente() {
		System.out.println("--- DATOS DEL CLIENTE ---");
		System.out.println("Nombre: " + nombre);
		System.out.println("Email: " + email);
	}
}