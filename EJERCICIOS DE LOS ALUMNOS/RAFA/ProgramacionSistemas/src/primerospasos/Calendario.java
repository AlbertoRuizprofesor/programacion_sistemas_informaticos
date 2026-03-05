package primerospasos;
import java.util.Scanner;

public class Calendario {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner c=new Scanner(System.in);
		
		System.out.print("cuanto tiempo dedicas al trabajo: ");
		int trabajo=c.nextInt();
		
		System.out.print("cuanto tiempo dedicas al dormir: ");
		int dormir=c.nextInt();
		
		System.out.print("cuanto tiempo dedicas a comer: ");
		int comer=c.nextInt();
		
		System.out.print("cuanto tiempo dedicas a reprochar: " );
		int reprochar=c.nextInt();
		
		System.out.print("cuanto tiempo dedicas a tele: " );
		int tele=c.nextInt();
		
		System.out.print("cuanto tiempo dedicas a hobbies: " );
		int hobbies=c.nextInt();
		
		System.out.print("cuanto tiempo dedicas a casa: " );
		int casa=c.nextInt();
		
		int trabajo_semanal=trabajo*7;
		System.out.println("dedicas a la semana al trabajo: "+trabajo);
		
		int dormir_semanal=dormir*7;
		System.out.println("dedicas a la semana a dormir: "+dormir);
		
		int comer_semanal=comer*7;
		System.out.println("dedicas a la semana a comer: "+comer);
		
		int reprochar_semanal=reprochar*7;
		System.out.println("dedicas a la semana al reproche: "+reprochar);
		
		int tele_semanal=tele*7;
		System.out.println("dedicas a la semana a tele: "+tele);
		
		int hobbies_semanal=hobbies*7;
		System.out.println("dedicas a la semana a hobbies: "+hobbies);
		
		int casa_semanal=casa*7;
		System.out.println("dedicas a la semana a la casa: "+casa);
		
		c.close();
	}

}
