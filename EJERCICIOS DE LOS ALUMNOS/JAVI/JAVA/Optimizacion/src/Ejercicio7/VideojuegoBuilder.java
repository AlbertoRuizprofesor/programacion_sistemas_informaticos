package Ejercicio7;

public class VideojuegoBuilder {
	private String nombre;
	private int anio;
	private double precio;
	private String plataforma;
	private String sinopsis;
	private String requerimientosMinimos;

	public VideojuegoBuilder nombre(String nombre) {
		this.nombre = nombre;
		return this;
	}

	public VideojuegoBuilder anio(int anio) {
		this.anio = anio;
		return this;
	}

	public VideojuegoBuilder precio(double precio) {
		this.precio = precio;
		return this;
	}

	public VideojuegoBuilder plataforma(String plataforma) {
		this.plataforma = plataforma;
		return this;
	}

	public VideojuegoBuilder sinopsis(String sinopsis) {
		this.sinopsis = sinopsis;
		return this;
	}

	public VideojuegoBuilder requerimientosMinimos(String requerimientosMinimos) {
		this.requerimientosMinimos = requerimientosMinimos;
		return this;
	}

	// El método clave que crea el objeto final
	public Videojuego build() {
		return new Videojuego(nombre, anio, precio, plataforma, sinopsis, requerimientosMinimos);
	}

}