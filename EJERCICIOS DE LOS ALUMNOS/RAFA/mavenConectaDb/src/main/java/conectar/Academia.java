package conectar;
import java.sql.*;
import java.util.Scanner;

public class Academia {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el nombre del curso: ");
        String nombreCurso = sc.nextLine();

        String url = "jdbc:mysql://localhost:3306/academia";
        String usuario = "root";
        String password = ""; // pon tu contraseña si tienes

        try {
            Connection conn = DriverManager.getConnection(url, usuario, password);

            // Consulta con parámetro
            String sql = "SELECT * FROM cursos WHERE nombre = ?";
            PreparedStatement ps = conn.prepareStatement(sql);

            // Usamos set (como en tu ejemplo)
            ps.setString(1, nombreCurso);

            ResultSet rs = ps.executeQuery();

            if (rs.next()) {
                System.out.println("\nCurso encontrado:");
                System.out.println("ID: " + rs.getInt("id"));
                System.out.println("Nombre: " + rs.getString("nombre"));
                System.out.println("Profesor: " + rs.getString("profesor"));
                System.out.println("Horas: " + rs.getInt("horas"));
            } else {
                System.out.println("El curso no existe.");
            }

            rs.close();
            ps.close();
            conn.close();

        } catch (SQLException e) {
            System.out.println("Error de conexión");
            e.printStackTrace();
        }

        sc.close();
    }
}
