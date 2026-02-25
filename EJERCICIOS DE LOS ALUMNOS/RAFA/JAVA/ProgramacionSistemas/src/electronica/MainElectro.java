package electronica;

public class MainElectro {
	public static void main(String[] args) {
		
		//Componentes componente=new Componentes("500 mW", "10 v", "50 mA");
		Transistores transistor=new Transistores("500 mW", "10 v", "50 mA", "BJT", "superficie");
		Condensadores condensador=new Condensadores("500 mW", "10 v", "50 mA", "eletrolitico", "polarizado");
		Inductancias inductancia=new Inductancias("500 mW", "10 v", "50 mA", "ferrita", "+-5%");
		//System.out.println(componente.toString());
		System.out.println(transistor.toString());
		System.out.println(condensador.toString());
		System.out.println(inductancia.toString());


	}

}
