package conectar;
import java.sql.*;
import java.util.Scanner;
public class Ejercicio7 {
	private static final String URL = "jdbc:mysql://localhost:3306/academia";
	private static final String USER = "root";
	private static final String PASS = "";

	    public static void main(String[] args) {
	        Scanner teclado = new Scanner(System.in);
	        int minHoras = 0;

	        // 1. Pedir datos con validación básica
	        System.out.print("Mostrar cursos con un mínimo de horas de: ");
	        if (teclado.hasNextInt()) {
	            minHoras = teclado.nextInt();
	        } else {
	            System.out.println("Error: Debes introducir un número entero.");
	            return; // Finaliza el programa si el dato es incorrecto
	        }

	        // 2. Sentencia SQL con el operador de comparación
	        String sql = "SELECT * FROM cursos WHERE horas >= ?";

	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql)) {

	            // 3. Asignar el valor al parámetro
	            ps.setInt(1, minHoras);

	            // 4. Ejecutar y recorrer los resultados
	            try (ResultSet rs = ps.executeQuery()) {
	                System.out.println("\n--- CURSOS DE " + minHoras + " HORAS O MÁS ---");
	                System.out.println("ID | NOMBRE | PROFESOR | HORAS");
	                System.out.println("---------------------------------");

	                boolean hayResultados = false;
	                while (rs.next()) {
	                    hayResultados = true;
	                    System.out.printf("%d | %s | %s | %d\n", 
	                        rs.getInt("id"), 
	                        rs.getString("nombre"), 
	                        rs.getString("profesor"), 
	                        rs.getInt("horas"));
	                }

	                if (!hayResultados) {
	                    System.out.println("No se encontraron cursos con esa duración.");
	                }
	            }

	        } catch (SQLException e) {
	            System.err.println("Error en la consulta: " + e.getMessage());
	        }
	    }
	}
