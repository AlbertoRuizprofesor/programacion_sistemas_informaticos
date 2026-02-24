package metodos;

public class MainImporte {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Importe importe=new Importe();
		int [] importar=importe.pedirDatos();
		importe.calculo_importe(importar);
		
	}

}
