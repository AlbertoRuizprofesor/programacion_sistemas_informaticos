package ejerciciosObligatoriosMetodos;

import java.util.Scanner;

public class mainNota {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Notas not=new Notas();
		Scanner s= new Scanner(System.in);
		System.out.print("dime tu nota: ");
        int a=s.nextInt();
        not.nota(a);
        
        s.close();
	}

}
