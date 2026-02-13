package metodos;
import java.util.Scanner;

public class MediaNotas {
// Entran datos
public void calculo_notas(int [] nota) { 
		
		// Variable suma para que se sumen las notas que se van metiendo
		int suma=0;
		for(int i=0;i<nota.length;i++) {
	
			suma+=nota[i];
		}
		System.out.println("La nota media es "+suma/nota.length);	
	}
	

	public int[] pedirDatos() {
		Scanner c=new Scanner(System.in);
		// Pedir 10 notas
		int [] numero=new int[10];
		
		for (int i=0;i<numero.length;i++) {
			System.out.print("Dime la nota "+(i+1)+" : ");
			numero[i]=c.nextInt();
		}
		
		c.close();
		return numero;
		
		
	}


}

