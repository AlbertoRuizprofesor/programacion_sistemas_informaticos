package observer2;

class Usuario implements Observer {
	private double umbral; // DEFINIMOS EL PARAMETRO UMBRAL

	public Usuario(double umbral) {
		this.umbral = umbral;
	}

	@Override // SOBREESCRIBIMOS EL METODO ACTUALIZAR DE LA INTERFAZ OBSERVER
	public void actualizar(double temperatura) {
		if (temperatura > umbral) {
			System.out.println("¡Alerta! La temperatura ha superado el umbral de " + umbral + " grados.");
		}
	}
}