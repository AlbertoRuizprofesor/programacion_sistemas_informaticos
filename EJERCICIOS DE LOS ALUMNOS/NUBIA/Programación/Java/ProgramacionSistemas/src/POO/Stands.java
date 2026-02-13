package POO;

public class Stands {
	private String nombre;
	private String usuario;
	
	public Stands (String nombre, String usuario) {
		this.nombre = nombre;
		this.usuario = usuario;
	}
	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre=nombre;
	}
	public String getUsuario (String usuario) {
		return usuario;
	}
	public void setUsuario(String usuario) {
		this.usuario=usuario;
	}
	@Override
	public String toString() {
		return "Stand: Nombre=" +nombre+ ", Usuario=" +usuario;
	}
}
