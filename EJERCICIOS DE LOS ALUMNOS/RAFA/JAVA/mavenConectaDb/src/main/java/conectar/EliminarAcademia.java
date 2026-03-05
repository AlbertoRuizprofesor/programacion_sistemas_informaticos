package conectar;
import java.sql.*;
import java.util.Scanner;

	public class EliminarAcademia {

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);

	        System.out.print("Ingrese el ID del curso a eliminar: ");
	        int id = sc.nextInt();

	        String url = "jdbc:mysql://localhost:3306/academia";
	        String usuario = "root";
	        String password = ""; // coloca tu contraseña si tienes

	        try {
	            Connection conn = DriverManager.getConnection(url, usuario, password);

	            // Sentencia DELETE con parámetro
	            String sql = "DELETE FROM cursos WHERE id = ?";
	            PreparedStatement ps = conn.prepareStatement(sql);

	            // Asignamos el valor al ?
	            ps.setInt(1, id);

	            // Ejecutamos
	            int filasEliminadas = ps.executeUpdate();

	            // Mostramos resultado
	            System.out.println("Filas eliminadas: " + filasEliminadas);

	            ps.close();
	            conn.close();

	        } catch (SQLException e) {
	            System.out.println("Error al eliminar el curso");
	            e.printStackTrace();
	        }

	        sc.close();
	    }
	}

