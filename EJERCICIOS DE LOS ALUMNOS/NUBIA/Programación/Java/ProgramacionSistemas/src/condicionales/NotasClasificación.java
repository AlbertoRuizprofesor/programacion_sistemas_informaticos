package condicionales;
import java.util.Scanner;

public class NotasClasificación {
	public static void main(String[] args) {
	
	Scanner c=new Scanner(System.in);
	

	System.out.println("RESULTADO DE NOTAS");
			
	System.out.print("Introduce tu nota: ");
	int nota = c.nextInt();
		
	if(nota<5) {
		System.out.println("Suspenso");		
	}
	else if(nota >= 5 && nota <=6) {
		System.out.println("Aprobado");
	}
	else if (nota >= 7 && nota <9){
		System.out.printf("Notable");
	}
	else if (nota >= 9 && nota==10) {
		System.out.print("Sobresaliente");
	}
	else {
		System.out.print("ERROR. Número fuera de rango");
	}
	c.close();
	}
}
