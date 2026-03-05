package metodos;

public class MainEdades {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Edades edades=new Edades();
		int []edad=edades.pedirDatos();
		edades.calcular_edades(edad);
		

	}

}
