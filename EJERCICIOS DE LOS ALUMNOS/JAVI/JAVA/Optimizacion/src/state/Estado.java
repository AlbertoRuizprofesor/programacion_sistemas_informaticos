package state;

//Interfaz del Estado
public interface Estado {
	void insertarMoneda();

	void devolverMoneda();

	void presionarBoton();

	void dispensar();
}
