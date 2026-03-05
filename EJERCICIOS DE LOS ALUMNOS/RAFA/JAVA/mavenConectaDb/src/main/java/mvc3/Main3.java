package mvc3;

import mvc3.Controlador3;

public class Main3 {
	public static void main(String[] args) {
	Alumnos modelo = new Alumnos(1,"rafa","aranda","programacion",11);
	Vista3 vista = new Vista3();
	Controlador3 controlador=new 
			Controlador3(modelo,vista);
	controlador.actualizarVista();
	}
}


