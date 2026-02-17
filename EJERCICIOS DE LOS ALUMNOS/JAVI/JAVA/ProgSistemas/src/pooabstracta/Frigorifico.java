package pooabstracta;

public class Frigorifico extends Electrodomestico {
	
	private int capacidad;
	private double altura;
	
	public Frigorifico(String color, int peso, String marca, String fabricante, double precio, int capacidad,
			double altura) {
		super(color, peso, marca, fabricante, precio);
		this.capacidad = capacidad;
		this.altura = altura;
	}

	public int getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}

	public double getAltura() {
		return altura;
	}

	public void setAltura(double altura) {
		this.altura = altura;
	}
	
	@Override
    void encender() {
        System.out.println("Encendiendo " + getMarca() + " con programa AUTO");
    }

    @Override
    void apagar() {
        System.out.println("Apagando " + getMarca() + " finalizado.");
    }

    @Override
    void comprar() {
        System.out.println("Comprando " + getMarca() + " ... compra realizada.");
    }
    
    @Override
    void devolver() {
        System.out.println("Devolviendo " + getMarca() + " ... devolución realizada.");
    }	
	

	@Override
	public String toString() {
		return "Frigorifico [Capacidad=" + getCapacidad() + ", Altura=" + getAltura() + ", Color="
				+ getColor() + ", Peso=" + getPeso() + ", Marca=" + getMarca() + ", Fabricante="
				+ getFabricante() + ", Precio=" + getPrecio() + "]";
	}
	
	
	
	
	
	
	
	
	
	

}
