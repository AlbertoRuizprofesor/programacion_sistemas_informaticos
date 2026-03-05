package poo;

public class MainVehiculo {
	public static void main(String[] args) {
		
		Coche coche=new Coche("Ferrari Rose","2000cc",5,"Rojo","Ferrari","Hibrido","gasolina","Si");
		Moto moto=new Moto("Ferrari Rose","2000cc",5,"Rojo","Ferrari","Hibrido","pedal","amarilla");
		Camiones camion=new Camiones("Ferrari Rose","2000cc",5,"Rojo","Ferrari","Hibrido","15000kg","Con remolque");
		
		System.out.println(coche.toString());
		coche.acelerar();
		coche.frenar();
		System.out.println(moto.toString());
		moto.acelerar();
		moto.frenar();
		System.out.println(camion.toString());
		camion.acelerar();
		camion.frenar();
	}
	
}
