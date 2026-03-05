package abstractaElectrodomesticos;

public class Frigorifico extends Electrodomestico {
	private String tipo;//frost o no frost

	public Frigorifico(String color, String peso, String marca, String fabricante, String precio, String tipo) {
		super(color, peso, marca, fabricante, precio);
		this.tipo=tipo;
	}

	public String getTipo() {
		return tipo;
	}

	public void setTipo(String tipo) {
		this.tipo = tipo;
	}

	@Override
	public String toString() {
		return "Frigorifico [tipo=" + tipo + ", getColor()=" + getColor() + ", getPeso()=" + getPeso() + ", getMarca()="
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
