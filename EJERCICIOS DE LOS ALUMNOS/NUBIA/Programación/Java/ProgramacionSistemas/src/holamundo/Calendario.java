package holamundo;
import java.util.Scanner;

public class Calendario {
	public static void main(String[] args) {
		Scanner c=new Scanner(System.in);
		
		
		System.out.println("¿Cuántas horas semanales dedicas a tus hobbies, salidas? ");
		int hobbies= c.nextInt();
		System.out.println("¿Cuántas dedicas a tareas de casa? ");
		int tareas= c.nextInt();
		System.out.println("¿Cuántas dedicas al trabajo? ");
		int trabajo= c.nextInt();
		System.out.println("¿Cuántas dedicas a dormir? ");
		int dormir= c.nextInt();
		System.out.println("¿Cuántas dedicas a comer? ");
		int comer= c.nextInt();
		System.out.println("¿Cuántas dedicas a reprochar? ");
		int reprochar= c.nextInt();
		
		int hobbiestotal= hobbies*4;
		System.out.println("Dedicas " +hobbiestotal+ " horas mensuales a hobbies");
		int tareastotal= tareas*4;
		System.out.println("Dedicas " +tareastotal+ " horas mensuales a tareas de casa");
		int trabajototal= trabajo*4;
		System.out.println("Dedicas " +trabajototal+ " horas mensuales al trabajo");
		int dormirtotal= dormir*4;
		System.out.println("Dedicas " +dormirtotal+ " horas mensuales a dormir");
		int comertotal= comer*4;
		System.out.println("Dedicas " +comertotal+ " horas mensuales a comer");
		int reprochartotal= reprochar*4;
		System.out.println("Dedicas " +reprochartotal+ " horas mensuales a reprochar");
		
		c.close();
		
		
	}

}
