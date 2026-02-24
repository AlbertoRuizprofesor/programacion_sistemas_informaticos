package gestiónFicheros;

import java.io.*;

public class CrearCarpeta {
	public static  void main(String[] args) {
		String ruta="C:\\";
		String carpeta="Ejercicio1";
		File directorio=new File(ruta+carpeta);
		
		if (directorio.exists()==true) {
			System.out.println("La carperta ya existe");
		}
		
		else {
			directorio.mkdir();
			System.out.println("Carpeta creada");
		}
	}

}
