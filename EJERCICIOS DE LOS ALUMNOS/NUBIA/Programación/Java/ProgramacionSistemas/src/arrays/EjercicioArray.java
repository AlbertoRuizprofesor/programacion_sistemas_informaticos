package arrays;

public class EjercicioArray {
	public static void main (String[] args) {
		int [] array=new int[10];
		
		String [] [] array2= {{"Nubia","20"}, {"Darío","16"}};
		System.out.println("Array multi");
		
		for (int a=0;a<array2.length;a++) {
			System.out.println("****");
			for (int b=0;b<array2.length;b++) {
				System.out.println("Posición "+a+b+" "+array2[a][b]);
			}
		}
	}

}
