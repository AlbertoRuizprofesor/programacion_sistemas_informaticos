package conectar;
import java.sql.*;
import java.util.Scanner;

public class HorasAcademia {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el ID del curso: ");
        int id = sc.nextInt();

        System.out.print("Ingrese el nuevo número de horas: ");
        int nuevasHoras = sc.nextInt();

        String url = "jdbc:mysql://localhost:3306/academia";
        String usuario = "root";
        String password = ""; // coloca tu contraseña si tienes

        try {
            Connection conn = DriverManager.getConnection(url, usuario, password);

            // Sentencia UPDATE con dos parámetros (como en tu ejemplo)
            String sql = "UPDATE cursos SET horas = ? WHERE id = ?";
            PreparedStatement ps = conn.prepareStatement(sql);

            // Usamos dos set
            ps.setInt(1, nuevasHoras);
            ps.setInt(2, id);

            // Ejecutamos
            int filasModificadas = ps.executeUpdate();

            // Mostramos resultado
            System.out.println("Filas modificadas: " + filasModificadas);

            ps.close();
            conn.close();

        } catch (SQLException e) {
            System.out.println("Error en la actualización");
            e.printStackTrace();
        }

        sc.close();
    }
}
