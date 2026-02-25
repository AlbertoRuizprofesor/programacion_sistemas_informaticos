package poo;

public class MainPersona {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Persona persona=new Persona("Alberto","Ruiz",134);
		Alumno alumno=new Alumno("Laura","Alicia",45,"primero","mates");
		Profesor profesor=new Profesor("Laura","Alicia",45,"primero","mates","lengua",1300);

		System.out.println(persona.toString());
		System.out.println(alumno.toString());
		System.out.println(profesor.toString());


	}

}
