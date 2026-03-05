package abstractaElectrodomesticos;

public class Lavadora extends Electrodomestico {
	private String carga;//frontal o superior

	public Lavadora(String color, String peso, String marca, String fabricante, String precio, String carga) {
		super(color, peso, marca, fabricante, precio);
		this.carga=carga;
	}

	public String getCarga() {
		return carga;
	}

	public void setCarga(String carga) {
		this.carga = carga;
	}

	@Override
	public String toString() {
		return "Lavadora [carga=" + carga + ", getColor()=" + getColor() + ", getPeso()=" + getPeso() + ", getMarca()="
				+ getMarca() + ", getFabricante()=" + getFabricante() + ", getPrecio()=" + getPrecio() + ", toString()="
				+ super.toString() + ", getClass()=" + getClass() + ", hashCode()=" + hashCode() + "]";
	}

	@Override
	void encender() {
		// TODO Auto-generated method stub
		System.out.println("encendido");
	}

	@Override
	void apagar() {
		// TODO Auto-generated method stub
		System.out.println("apagado");
	}

	@Override
	void comprar() {
		// TODO Auto-generated method stub
		System.out.println("comprado");
	}

	@Override
	void devolver() {
		// TODO Auto-generated method stub
		System.out.println("devuelto");
	}
	
}
