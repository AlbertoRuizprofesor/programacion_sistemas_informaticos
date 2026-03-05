package conectar;
import java.sql.*;
import java.util.Scanner;

public class BuscarCursoNombre {

    private static final String URL = "jdbc:mysql://localhost:3306/academia";
    private static final String USER = "root";
    private static final String PASS = "";

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Introduce el nombre del curso a buscar: ");
        String nombreBuscar = sc.nextLine();

        // marcador de posición '?'
        String sql = "SELECT * FROM cursos WHERE nombre = ?";

        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
             PreparedStatement ps = con.prepareStatement(sql)) {

            // rellenamos el marcador (índice 1)
            ps.setString(1, nombreBuscar);

            // ejecutamos la consulta
            try (ResultSet rs = ps.executeQuery()) {
                
                // comprobamos resultados
                if (rs.next()) {
                    System.out.println("\n--- CURSO ENCONTRADO ---");
                    System.out.println("ID: " + rs.getInt("id"));
                    System.out.println("NOMBRE: " + rs.getString("nombre"));
                    System.out.println("PROFESOR: " + rs.getString("profesor"));
                    System.out.println("HORAS: " + rs.getInt("horas"));
                } else {
                    System.out.println("No existe ningún curso con el nombre: " + nombreBuscar);
                }
            }

        } catch (SQLException e) {
            System.err.println("Error de base de datos: " + e.getMessage());
        }
        sc.close();
    }
}