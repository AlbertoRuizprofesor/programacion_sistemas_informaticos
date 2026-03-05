
package metodos;

import java.util.Scanner;

public class Importe {

	public void calculo_importe(int [] importe) {
		
		int suma=0;
		for(int i=0;i<importe.length;i++) {
	
			suma+=importe[i];
		}
		double iva=suma*0.21;
		
	public void calculo_notas(int [] nota) {
		
		int suma=0;
		for(int i=0;i<nota.length;i++) {
	
			suma+=nota[i];
		}
		System.out.println("la nota media es:"+suma/nota.length);
		
		
	}
	

	public int[] pedirDatos() {
		Scanner c=new Scanner(System.in);
		int [] numero=new int[10];
		
		for (int i=0;i<numero.length;i++) {
			System.out.print("Dime la nota "+(i+1)+" : ");
			numero[i]=c.nextInt();
		}
		
		c.close();
		return numero;
		
		
	}


}