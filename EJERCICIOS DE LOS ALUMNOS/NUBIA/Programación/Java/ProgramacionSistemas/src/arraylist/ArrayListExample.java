package arraylist;
import java.util.ArrayList; //Importar herramienta Array

public class ArrayListExample {
	public static void main(String[] args) {
		
		ArrayList<Integer> edad=new ArrayList<>(); //Crear array "lista"
		ArrayList<String> nombre=new ArrayList<>(); //Crear array "nombre"
		ArrayList<Double> ingresos=new ArrayList<>();
		
		edad.add(10); //Agregación de elementos al array "lista"
		edad.add(20);
		edad.add(30);
		
		nombre.add("Nubia"); //Agregación de nombres al array "nombre"
		nombre.add("Ana");
		nombre.add("Noemi");
		
		ingresos.add(3500.00);
		ingresos.add(2000.00);
		ingresos.add(2700.00);
		
		
		for (int age:edad) { //Bucle para imprimir todos los elementos de la lista
			// age hace referencia a cada elemento del array, edad al propio array
			System.out.println("Edad "+edad); 
		}
		
		for (String name:nombre) { 
			System.out.println("Nombre "+nombre);
		}
		
		for (double ing:ingresos) {
			System.out.println("Ingresos "+ingresos);
		}
	}

}
