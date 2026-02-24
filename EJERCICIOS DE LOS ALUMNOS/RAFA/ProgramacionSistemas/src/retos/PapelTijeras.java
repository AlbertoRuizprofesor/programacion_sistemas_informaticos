package retos;
import java.math.*;
import java.util.Scanner;

public class PapelTijeras {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int n=(int)(Math.random()*3)+1;
		//System.out.print(n);
		
		if (n==1) {
			System.out.print("Piedra");
		}else if(n==2) {
			System.out.print("Papel");
		}else {
			System.out.print("Tijeras");
		}
	}

}
