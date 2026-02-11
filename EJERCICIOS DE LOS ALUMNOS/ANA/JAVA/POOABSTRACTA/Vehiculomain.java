package POOABSTRACTA;

public class Vehiculomain {
 public static void main (String[] args) {
	 Coche [] coche=new Coche[2];
	 
	 Camion c = new Camion("verde",4,"Iveco","Si","V8");
	 Moto m = new Moto("si",2,"V4","si");
			 
	 coche[0]=new Coche("rojo",4,"Ferrarri" , 9000);
	 coche[1]=new Coche("azul",4,"BMW",7000);
	 
	 for(Coche car:coche) {
		 System.out.println(car);
		 car.acelerar();
		 car.frenar();
		 car.aparcar();
	 	}
	 	System.out.println(c.toString());
	 	System.out.println(m.toString());
	 
 	}
}
