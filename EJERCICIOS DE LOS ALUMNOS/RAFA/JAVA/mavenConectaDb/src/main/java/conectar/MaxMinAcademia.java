package conectar;
import java.sql.*;
import java.util.Scanner;

	public class MaxMinAcademia {

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        System.out.print("Ingrese el número mínimo de horas: ");
	        int horasMinimas = sc.nextInt();

	        String url = "jdbc:mysql://localhost:3306/academia";
	        String usuario = "root";
	        String password = ""; // coloca tu contraseña si tienes

	        try {
	            Connection conn = DriverManager.getConnection(url, usuario, password);

	            // Consulta con parámetro
	            String sql = "SELECT * FROM cursos WHERE horas >= ?";
	            PreparedStatement ps = conn.prepareStatement(sql);

	            // Asignamos el valor al ?
	            ps.setInt(1, horasMinimas);

	            ResultSet rs = ps.executeQuery();

	            System.out.println("\nCursos con " + horasMinimas + " horas o más:\n");

	            boolean encontrado = false;

	            while (rs.next()) {
	                encontrado = true;
	                System.out.println("ID: " + rs.getInt("id") +
	                                   " | Nombre: " + rs.getString("nombre") +
	                                   " | Profesor: " + rs.getString("profesor") +
	                                   " | Horas: " + rs.getInt("horas"));
	            }

	            if (!encontrado) {
	                System.out.println("No hay cursos con esa cantidad de horas.");
	            }

	            rs.close();
	            ps.close();
	            conn.close();

	        } catch (SQLException e) {
	            System.out.println("Error en la consulta");
	            e.printStackTrace();
	        }

	        sc.close();
	    }
	}

