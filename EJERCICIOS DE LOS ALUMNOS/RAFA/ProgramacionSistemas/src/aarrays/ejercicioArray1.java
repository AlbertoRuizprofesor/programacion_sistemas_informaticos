package aarrays;

public class ejercicioArray1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] array1= {1,34,56,67};
		/* En java no puedes crear arrays de diferentes tipos, una manera
		   es crear una array de texto y despues parsear por ejemplo los numeros 	
		*/
		String [] array2= {"Albert","12","Laura","17"};
		
		String [] array3= new String[5];
		
		int [] array4= new int[5];
		
		System.out.println("array 1 con bucle for");
		for (int i=0;i<3;i++) {
			System.out.println(array1[i]);
			
		}
		
		//en vez de usar i<3 usaremos length
		System.out.println("array 1 con bucle for y length***********");
		for (int i=0;i<array1.length;i++) {
			System.out.println(array1[i]);
		
		}
		System.out.println("array 1 con bucle for each************");
		//usando bucles for each
		for (int y:array1) {
			System.out.println(y);
			
		}
		
		//parsear con un array
		System.out.println("array 1 con bucle for y parseo************");
		
		int suma=0;
		for (int i=1;i<array2.length;i+=2) {
			
			array4[i]= Integer.parseInt(array2[i]);
			System.out.println("el valor n es "+array4[i]);
			suma+=array4[i];
			
		}
		System.out.println("la suma es "+suma);
		
		System.out.println("array 3 vacio y añadir datos, luego mostrar datos con bucle for each***");
		array3[0]="Hola";
		array3[1]="Mundo";
		
		for (String z:array3) {
			System.out.println(z);
		}
		
		System.out.println("intentando que no salgan los null********");
		int i=0;
		while(array3[i]!=null) {
			System.out.println(array3[i]);
			
		i++;	
		}
		
		
		String[][] array5= {{"albert","12"},{"laura","17"}};
		System.out.println("array multi");
		
		for(int a=0;a<array5.length;a++) {
			System.out.println("******");
			for (int b=0;b<array5.length;b++) {
				System.out.println("posicion"+a+b+" "+array5[a][b]);
			}
		}
	}
}
		