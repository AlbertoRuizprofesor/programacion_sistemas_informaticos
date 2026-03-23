package ejercicio10;

public class Movil {
	private String marca;
	private String modelo;
	private int bateria; // Valor de 0 a 100

	public Movil(String marca, String modelo, int bateriaInicial) {
		this.marca = marca;
		this.modelo = modelo;
		// Validamos que no empiece con valores imposibles
		if (bateriaInicial > 100)
			this.bateria = 100;
		else if (bateriaInicial < 0)
			this.bateria = 0;
		else
			this.bateria = bateriaInicial;
	}

	// Método para cargar: no puede pasar de 100
	public void cargarBateria(int cantidad) {
		this.bateria += cantidad;
		if (this.bateria > 100) {
			this.bateria = 100;
		}
		System.out.println("Cargando... Batería actual: " + this.bateria + "%");
	}

	// Método para usar: no puede bajar de 0
	public void usarBateria(int cantidad) {
		this.bateria -= cantidad;
		if (this.bateria < 0) {
			this.bateria = 0;
			System.out.println("¡Aviso! El móvil se ha apagado.");
		}
		System.out.println("Usando móvil... Batería restante: " + this.bateria + "%");
	}

	public void mostrarEstado() {
		System.out.println("----- ESTADO DEL MÓVIL -----");
		System.out.println("Dispositivo: " + marca + " " + modelo);
		System.out.println("Carga actual: " + bateria + "%");
		System.out.println("----------------------------");
	}
}