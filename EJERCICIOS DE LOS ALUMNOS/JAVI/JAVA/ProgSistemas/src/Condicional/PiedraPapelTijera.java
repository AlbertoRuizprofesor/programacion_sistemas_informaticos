package Condicional;

public class EjercicioNotas {

	public static void main(String[] args) {
		
		int num1 = 0, num2 = 0, num3 = 0;
		
		System.out.println(num1 + "-" + num2 + "-" + num3);
		int n =(int)(Math.random()*3) + 1;
		System.out.print(n);
		
		int nota = 5;
		
		if(nota<5) {
			System.out.print("Estás suspenso.");
		}
		
	}

}
