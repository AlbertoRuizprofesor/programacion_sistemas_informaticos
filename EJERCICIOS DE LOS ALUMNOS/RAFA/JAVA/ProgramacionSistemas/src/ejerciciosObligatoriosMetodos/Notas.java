package ejerciciosObligatoriosMetodos;

public class Notas {
	public int nota(int a) {
		if (a<=4){
			System.out.println(" estas suspenso");
		}else if (a>=4 && a<=5) {
			System.out.println(" suficiente");
		}else if (a==6) {
            System.out.println(" bien");
		}else if (a>=7 && a<=8) {
            System.out.println(" notable");
		}else if (a>=9 && a<=10) {
            System.out.println(" notable");
		}else {
            System.out.println("prueba del 0 al 10");
        }
	return a;
	}

}