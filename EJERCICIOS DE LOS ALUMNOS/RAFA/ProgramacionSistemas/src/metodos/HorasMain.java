package metodos;
import java.util.Scanner;

public class HorasMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Horas hor=new Horas();
		Scanner s= new Scanner(System.in);
		System.out.print("dime los dias: ");
        int dias=s.nextInt();
        hor.calculoHoras(dias);
        hor.calculoMinutos(horas);
	}
}
