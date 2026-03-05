package metodos;


public class MainOperacionesArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
				
		OperacionesArray operaciones=new OperacionesArray();
		int [] numero=operaciones.pedirDatos();
		operaciones.lista_Operaciones(numero[0],numero[1]);
		
		
		
		
	}


}


/*

package metodos;
public class MainOperacionesArray{
	public static void main(String[] args){
	
	OperacionesArray operaciones=new OperacionesArray();
	int[] numero=operaciones.pedirDatos();
	operaciones.lista_operaciones(numero[0],numero[1];
	}
}

*/