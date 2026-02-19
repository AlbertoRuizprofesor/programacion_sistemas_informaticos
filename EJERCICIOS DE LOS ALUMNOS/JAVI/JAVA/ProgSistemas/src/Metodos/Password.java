package Metodos;


/* Crea un ejercicio que me pida el usuario y el password, controla con un método que el password,
 *  sea de un mínimo de 8 caracteres, y otro para el password que no sea igual al usuario.
 */


public class Password {
	
	//ATRIBUTOS
	public String user;
	public String password;
	
	
	public boolean esValida() {
	    // Si es igual al usuario O tiene menos de 8 caracteres, no es válida
	    if (password.equals(user) || password.length() < 8) {
	        return false;
	    }
	    return true;
	}

	public void mostrar() {
	    if (esValida()) { // Si es true...
	        System.out.println("Password aceptado.");
	    } else { // Si es false...
	        System.out.println("Password no válido.");
	    }
	}
		
		
	}

