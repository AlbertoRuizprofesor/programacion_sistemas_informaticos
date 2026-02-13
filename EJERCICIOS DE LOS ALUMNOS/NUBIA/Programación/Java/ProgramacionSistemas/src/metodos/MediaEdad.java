package metodos;

import java.util.Scanner;

public class MediaEdad {

	public void calculo_edad(int [] edad) {
			int suma=0;
			for(int i=0;i<edad.length;i++) {
				suma+=edad[i];

				if (edad[i]< 18) {
					System.out.println("¿"+edad[i]+"?"+" Eres menor de edad ");
				}
				else {
					System.out.println("¿"+edad[i]+"?"+" Eres mayor de edad ");
				}
			}
			System.out.println("La edad media es "+suma/edad.length);
	}
	

	public int[] pedirDatos() {
		Scanner c=new Scanner(System.in);
		int [] numero=new int[10];
		
		for (int i=0;i<numero.length;i++) {
			System.out.print("Dime la edad "+(i+1)+" : ");
			numero[i]=c.nextInt();
		}
		
		c.close();
		return numero;
	}
}
