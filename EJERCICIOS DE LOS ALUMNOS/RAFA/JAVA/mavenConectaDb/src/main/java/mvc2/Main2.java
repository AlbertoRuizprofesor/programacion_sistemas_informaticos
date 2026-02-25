package mvc2;
public class Main2 {


		public static void main(String[] args) {
			Productos modelo = new Productos(1,"movil",1200);
			Vista2 vista = new Vista2();
			Controlador2 controlador=new 
					Controlador2(modelo,vista);
			controlador.actualizarVista();
			}

}

