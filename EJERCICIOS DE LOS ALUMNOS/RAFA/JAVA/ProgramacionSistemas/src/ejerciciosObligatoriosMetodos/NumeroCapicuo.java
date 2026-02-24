package ejerciciosObligatoriosMetodos;

import java.util.Scanner;

public class NumeroCapicuo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s= new Scanner(System.in);
		System.out.print("indica el primer número; ");     
        int a=s.nextInt();
		System.out.println("¿es capicua? "+esCapicua(a));
		

	}
	public static boolean esCapicua(int x) {
		boolean capicua=false;
	    if (x%10==x/10) {
			capicua=true;
		}else{
			capicua=false;
		}
		return capicua;
    }


}