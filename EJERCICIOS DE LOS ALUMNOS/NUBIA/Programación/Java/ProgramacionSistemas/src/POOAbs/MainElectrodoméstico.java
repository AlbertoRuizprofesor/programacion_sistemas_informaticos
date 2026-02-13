package POOAbs;

public class MainElectrodoméstico {
	public static void main (String[] args) {
		
		Lavadora [] lavadoras=new Lavadora[2];
		lavadoras[0]=new Lavadora("blanca", 65, "Hisense", "Grupo Hisense", 850, "frontal", 12);
		lavadoras[1]=new Lavadora("gris", 70, "LG", "LG Company", 900, "superior", 15);
		
		Cafetera [] cafeteras=new Cafetera[2];
		cafeteras[0]=new Cafetera("verde", 7, "Siemens", "De'Longhi S.p.A.", 500 , "Superautomática");
		
		Frigo [] frigos=new Frigo[2];
		frigos[0]=new Frigo("gris", 70, "Bosh", "BSH Hausgeräte GmbH", 800, "300L", 1.86);
		
		for (Lavadora l : lavadoras) {
		    if (l != null) { //evitar NullPointerException si el array no está lleno
		        System.out.println(l.toString());
		        }
		}
		for (Cafetera l : cafeteras) {
		    if (l != null) { 
		        System.out.println(l.toString());
		        }
		}
		for (Frigo l : frigos) {
		    if (l != null) { 
		        System.out.println(l.toString());
		        }
		}
	}
}
	
