package POO;

public class MainStands {
	public static void main(String [] args) {
		
		Stands stand=new Stands("The World", "Dio Brando"); //Clase padre
		System.out.println(stand.toString());
		
		StandsCombate fuerza=new StandsCombate("The World", "Dio Brando", "SS"); //Clase hija
		System.out.println(fuerza.toString());
		
		StandsHabi habilidad=new StandsHabi("The World", "Dio Brando", "SS", "Detener el tiempo 11s"); //Clase nieta
		System.out.println(habilidad.toString());
		
		//Ejemplo de clase nieta (que hereda de clase hija, a la vez de clase padre)
		StandsHabi habi1=new StandsHabi("Heaven's Door", "Rohan Kishibe", "S",
				"Lectura y sobreescritura de recuerdos y habilidades");
		System.out.println(habi1.toString());
	}
}
