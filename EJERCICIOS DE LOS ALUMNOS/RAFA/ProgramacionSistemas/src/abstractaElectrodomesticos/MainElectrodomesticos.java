package abstractaElectrodomesticos;

public class MainElectrodomesticos {
	public static void main(String[] args) {
		//LAVADORA
		Lavadora [] lavadora=new Lavadora[2];
		lavadora[0]=new Lavadora("White", "20 kg", "Deluxe", "Siemens", "450€", "5 kg");
		lavadora[1]=new Lavadora("White/Gray", "25 kg", "Deluxe", "Siemens", "570€", "7 kg");
		for(Lavadora siemens:lavadora) {
			System.out.println(siemens);
			//siemens.encender();
			siemens.apagar();
			//siemens.comprar();
			//siemens.devolver();
		}
		//CAFETERA
		Cafetera [] cafetera=new Cafetera[2];
		cafetera[0]=new Cafetera("White", "20 kg", "Deluxe", "Siemens", "450€", "electrica");
		cafetera[1]=new Cafetera("White/Gray", "25 kg", "Deluxe", "Siemens", "570€", "standard");
		for(Cafetera miele:cafetera) {
			System.out.println(miele);
			//miele.encender();
			//miele.apagar();
			miele.comprar();
			//miele.devolver();
		}
		//FRIGORIFICO
		Frigorifico [] frigorifico=new Frigorifico[2];
		frigorifico[0]=new Frigorifico("White", "20 kg", "Deluxe", "Siemens", "450€", "Frost");
		frigorifico[1]=new Frigorifico("White/Gray", "25 kg", "Deluxe", "Siemens", "570€", "No Frost");
		for(Frigorifico balay:frigorifico) {
			System.out.println(balay);
			balay.encender();
			//balay.apagar();
			//balay.comprar();
			//balay.devolver();
		}
	}
}
		



