package POO;

public class MainVehículo {
	public static void main(String[] args) {
		
		Coche coche=new Coche("Renault", "Twingo", "Negro");
		Moto moto=new Moto("Honda", "PCX", "125");
		Camión camion=new Camión("Iveco", "S-Way", "Ligero");
		
		System.out.println(coche.toString());
		System.out.println(moto.toString());
		System.out.println(camion.toString());
	}
}
