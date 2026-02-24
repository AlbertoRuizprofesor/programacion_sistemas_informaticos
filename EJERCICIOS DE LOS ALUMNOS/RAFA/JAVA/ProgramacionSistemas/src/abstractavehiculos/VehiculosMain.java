package abstractavehiculos;

public class VehiculosMain {
	public static void main(String[] args) {
		Coche [] coche=new Coche[2];
		coche[0]=new Coche("verde",4,"Ferrari",9000);
		coche[1]=new Coche("rojo",4,"BMW",7000);
		for(Coche car:coche) {
			System.out.println(car);
			car.acelerar();
			car.frenar();
			car.aparcar();
		}
	}

}
