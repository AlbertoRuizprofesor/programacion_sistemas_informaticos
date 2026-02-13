package metodos;

public class CalcularMedia {
			
	public int sumar(int nota1, int nota2, int nota3) {
		return nota1+nota2+nota3;
	}
	public int calcularmedia(int nota1, int nota2, int nota3) {
		return sumar(nota1, nota2, nota3)/3;
	}
	
	public void mostrarMedia(int nota1, int nota2, int nota3) {
		double media=calcularmedia(nota1, nota2, nota3);
		System.out.println("La media es "+media);
	}	
}
