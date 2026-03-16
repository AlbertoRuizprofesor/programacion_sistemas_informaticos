package factory2;

class Profesores implements Persona {
	@Override
	public void accion() {
		System.out.println("El profesor está enseñando");
	}
}
