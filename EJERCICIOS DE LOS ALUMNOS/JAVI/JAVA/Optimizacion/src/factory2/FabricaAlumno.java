package factory2;

class FabricaAlumno extends Fabrica {
	@Override
	public Persona crearPersona() {
		return new Alumno();
	}
}
