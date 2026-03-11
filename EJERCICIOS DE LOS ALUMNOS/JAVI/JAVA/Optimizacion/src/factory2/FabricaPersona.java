package factory2;

class FabricaProfesores extends Fabrica {
	@Override
	public Persona crearPersona() {
		return new Profesores();
	}
}
