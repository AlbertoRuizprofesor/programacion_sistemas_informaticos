package metodos;

public class MainMediaEdad {
	public static void main(String[] args) {
		
		MediaEdad edades=new MediaEdad();
		int [] edad=edades.pedirDatos();
		edades.calculo_edad(edad);
	}
}