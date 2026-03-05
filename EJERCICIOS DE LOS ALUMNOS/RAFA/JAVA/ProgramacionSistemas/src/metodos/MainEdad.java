package metodos;

import java.util.Scanner;

public class MainEdad {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ObjetoEdad eda=new ObjetoEdad();
		Scanner s= new Scanner(System.in);
		System.out.print("dime tu año nacimiento: ");
        int a=s.nextInt();
        eda.edad(a);
        eda.datos("rafa","aranda");
        
        s.close();
	}

}
