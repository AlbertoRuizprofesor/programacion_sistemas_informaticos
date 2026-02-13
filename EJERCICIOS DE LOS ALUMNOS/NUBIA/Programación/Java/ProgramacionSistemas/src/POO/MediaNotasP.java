package POO;
import java.util.Scanner;

public class MediaNotasP {
	public void calculo_notas( int[] nota) { //creamos array donde se hará la suma de notas almacenadas
		
		int suma=0; //aquí se almacenará el total de la suma
		for (int i=0;i<nota.length;i++) {
			suma = suma+nota[i]; //aquí se suma al total el nuevo número
		}
		System.out.println("La media es "+suma/nota.length); // suma/nota.length realiza la media y la muestra
	}
	public int[] pedirDatos() { //método para pedir las notas
		Scanner sc=new Scanner(System.in); //escáner para pedir la nota
		int[] numero=new int[10]; //array para almacenar las notas (límite 10 notas)
		
		for (int i=0;i<numero.length;i++) { //bucle para pedir nota1, nota2, nota3, nota4...
			System.out.print("Dime la nota "+(i+1)+": ");
			numero[i]=sc.nextInt(); //se añade la nota cuando se pulse ENTER	
		}
		sc.close(); //cerrar escáner
		return numero;
	}

}
