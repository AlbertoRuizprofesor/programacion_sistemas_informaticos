package POOVIDEOJUEGOS;

public class WoW_main {

	public static void main(String[] args) {

		worldofwarcraft w = new worldofwarcraft("100", "3724", "Horda");
		Jainavaliente j = new Jainavaliente("100", "300", "Alianza", "si", "si");
		Anduinwrynn a = new Anduinwrynn("350", "15", "Alianza", "si", "si");
		Sylvanasbrisaveloz s = new Sylvanasbrisaveloz("200", "100", "Horda", "si", "si");
		Lorthemartheron l = new Lorthemartheron("400", "200", "Horda", "si", "si");
		
		System.out.println(w.toString());
		System.out.println(j.toString());
		System.out.println(a.toString());
		System.out.println(s.toString());
		System.out.println(l.toString());
		
		//Metodo de la clases worldofwarcraft que despues se modifica en jainavaliente
		//devuelve una cadena por pantalla 
		w.intelecto();
		j.intelecto();
		a.intelecto();
		s.intelecto();
		l.intelecto();

	}

}
