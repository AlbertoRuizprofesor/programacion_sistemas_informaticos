package template;

public class EjemploPatronMetodoPlantilla {
	public static void main(String[] args) {
		BebidaConCafeina te = new Te();
		te.prepararReceta(); // Prepara el té siguiendo los pasos de la receta

		BebidaConCafeina cafe = new Cafe();
		cafe.prepararReceta(); // Prepara el café siguiendo los pasos de la receta
	}
}
