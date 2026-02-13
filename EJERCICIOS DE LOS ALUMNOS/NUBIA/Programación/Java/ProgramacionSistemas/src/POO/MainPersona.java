package POO;

public class MainPersona {
	public static void main(String [] args) {
		
		Persona persona=new Persona("Nubia", "Montesinos", 20);
		Alumno alumno=new Alumno("Darío", "Villena", 17, "1º Bach", "Mates");
		Profesor profesor=new Profesor("Alberto", "Ruiz", 56, "Informática", 3000);
		
		System.out.println(persona.toString());
		System.out.println(alumno.toString());
		System.out.println(profesor.toString());
	}
}
