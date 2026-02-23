package conectar;
import java.sql.*;
import java.util.Scanner;
public class EjercicioFinal {


	    // conexión
	    private static final String URL = "jdbc:mysql://localhost:3306/academia";
	    private static final String USER = "root";
	    private static final String PASS = "";
	    private static Scanner teclado = new Scanner(System.in);

	    public static void main(String[] args) {
	        int opcion = -1;

	        do {
	            System.out.println("\n--- MENÚ GESTIÓN ACADEMIA ---");
	            System.out.println("1. Insertar curso");
	            System.out.println("2. Mostrar todos los cursos");
	            System.out.println("3. Buscar curso por nombre");
	            System.out.println("4. Actualizar horas de un curso");
	            System.out.println("5. Eliminar curso");
	            System.out.println("0. Salir");
	            System.out.print("Selecciona una opción: ");

	            try {
	                opcion = Integer.parseInt(teclado.nextLine()); // Evitamos problemas de buffer del Scanner

	                switch (opcion) {
	                    case 1: insertar(); break;
	                    case 2: mostrar(); break;
	                    case 3: buscar(); break;
	                    case 4: actualizar(); break;
	                    case 5: eliminar(); break;
	                    case 0: System.out.println("Saliendo del sistema..."); break;
	                    default: System.out.println("Opción no válida.");
	                }
	            } catch (NumberFormatException e) {
	                System.out.println("Error: Introduce un número válido.");
	            }
	        } while (opcion != 0);
	    }

	    // 1. INSERTAR
	    private static void insertar() {
	        System.out.print("Nombre del curso: ");
	        String nombre = teclado.nextLine();
	        System.out.print("Nombre del profesor: ");
	        String profe = teclado.nextLine();
	        System.out.print("Número de horas: ");
	        int horas = Integer.parseInt(teclado.nextLine());

	        String sql = "INSERT INTO cursos (nombre, profesor, horas) VALUES (?, ?, ?)";
	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql)) {
	            ps.setString(1, nombre);
	            ps.setString(2, profe);
	            ps.setInt(3, horas);
	            ps.executeUpdate();
	            System.out.println("✅ Curso insertado con éxito.");
	        } catch (SQLException e) { System.out.println("Error: " + e.getMessage()); }
	    }

	    // 2. MOSTRAR
	    private static void mostrar() {
	        String sql = "SELECT * FROM cursos";
	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql);
	             ResultSet rs = ps.executeQuery()) {
	            
	            System.out.println("\nID | CURSO | PROFESOR | HORAS");
	            while (rs.next()) {
	                System.out.printf("%d | %s | %s | %d\n", rs.getInt("id"), rs.getString("nombre"), rs.getString("profesor"), rs.getInt("horas"));
	            }
	        } catch (SQLException e) { System.out.println("Error: " + e.getMessage()); }
	    }

	    // 3. BUSCAR
	    private static void buscar() {
	        System.out.print("Nombre del curso a buscar: ");
	        String buscar = teclado.nextLine();
	        String sql = "SELECT * FROM cursos WHERE nombre LIKE ?"; // Usamos LIKE para búsquedas flexibles
	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql)) {
	            ps.setString(1, "%" + buscar + "%");
	            ResultSet rs = ps.executeQuery();
	            while (rs.next()) {
	                System.out.println("Encontrado: " + rs.getString("nombre") + " - Prof: " + rs.getString("profesor"));
	            }
	        } catch (SQLException e) { System.out.println("Error: " + e.getMessage()); }
	    }

	    // 4. ACTUALIZAR
	    private static void actualizar() {
	        System.out.print("ID del curso a modificar: ");
	        int id = Integer.parseInt(teclado.nextLine());
	        System.out.print("Nuevas horas: ");
	        int horas = Integer.parseInt(teclado.nextLine());

	        String sql = "UPDATE cursos SET horas = ? WHERE id = ?";
	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql)) {
	            ps.setInt(1, horas);
	            ps.setInt(2, id);
	            int filas = ps.executeUpdate();
	            System.out.println(filas > 0 ? "Actualizado." : "No encontrado.");
	        } catch (SQLException e) { System.out.println("Error: " + e.getMessage()); }
	    }

	    // 5. ELIMINAR
	    private static void eliminar() {
	        System.out.print("ID del curso a borrar: ");
	        int id = Integer.parseInt(teclado.nextLine());
	        String sql = "DELETE FROM cursos WHERE id = ?";
	        try (Connection con = DriverManager.getConnection(URL, USER, PASS);
	             PreparedStatement ps = con.prepareStatement(sql)) {
	            ps.setInt(1, id);
	            int filas = ps.executeUpdate();
	            System.out.println(filas > 0 ? "Eliminado." : "ID no existe.");
	        } catch (SQLException e) { System.out.println("Error: " + e.getMessage()); }
	    }
	}
