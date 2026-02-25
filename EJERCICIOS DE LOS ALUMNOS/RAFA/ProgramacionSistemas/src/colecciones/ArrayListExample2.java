package colecciones;

import java.util.ArrayList;

public class ArrayListExample2 {
	 public static void main(String[] args) {
		 ArrayList<Integer> numeros=new ArrayList<>();
		 numeros.add(10);
		 numeros.add(20);
		 numeros.add(30);
		 System.out.println("lista creada "+numeros);
		 System.out.println("antes de remove "+numeros.size());
		 System.out.println("aplico remove "+numeros.remove(1));
		 System.out.println("despues de remove "+numeros.size());
		 System.out.println("lista ahora "+numeros);
		 
		 System.out.println("posicion de 30 "+numeros.indexOf(30));

		 boolean encontrar;
		 int valor=30;
		 if(numeros.contains(valor)==true) {
			 System.out.println("la posicion del valor es:  "+numeros.indexOf(valor));
		 }else {
			 System.out.println("no encontrado");
		 }
	        buscar(numeros,30);
	    }
	    
	    public static void buscar(ArrayList<Integer> numer, int element) {
	    	
	    	if(numer.contains(element)) {
	    		System.out.println("encontrado la posicion es "+numer.indexOf(element));
	    		
	    	}else {
	    		System.out.println("no encontrado en verdad, tengo hambre");
	    			
	    	}


	

	   modificar(numer,30,2000);
	    }
	    
	   public static void modificar(ArrayList<Integer> numer, int element, 
			   int cambiar) {
	    	
	    	if(numer.contains(element)) {
	    		System.out.println("encontrado "+element+
	    	" modificado con "+cambiar);
	    		numer.set(numer.indexOf(element), cambiar);
	    		System.out.println(numer);
	    		
	    	}else {
	    		System.out.println("no encontrado en verdad, tengo hambre");
	    			
	    	}
	   }
}


	

