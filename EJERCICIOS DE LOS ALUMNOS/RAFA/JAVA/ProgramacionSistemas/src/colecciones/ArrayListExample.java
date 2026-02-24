package colecciones;

import java.util.ArrayList;

public class ArrayListExample {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ArrayList<Integer> lista=new ArrayList<>();
		ArrayList<String> nombres=new ArrayList<>();
		ArrayList<Double> ingresos=new ArrayList<>();
		
		lista.add(10);
		lista.add(20);
		
		nombres.add("alberto");
		nombres.add("laura");
		nombres.remove(1);
		
		ingresos.add(1200.00);
		ingresos.add(1300.00);
		
		for (int list : lista) {
		    System.out.println(list);
		}
		for (String nomb : nombres) {
		    System.out.println(nomb);
		}
		for (Double ingr : ingresos) {
		    System.out.println(ingr);
		}

	}

}
