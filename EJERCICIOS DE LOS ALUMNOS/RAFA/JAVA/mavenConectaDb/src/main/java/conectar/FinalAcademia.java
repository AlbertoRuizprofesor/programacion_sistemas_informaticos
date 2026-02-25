package conectar;
import java.sql.*;
import java.util.Scanner;

	public class FinalAcademia {

	    static final String URL = "jdbc:mysql://localhost:3306/academia";
	    static final String USER = "root";
	    static final String PASSWORD = ""; // coloca tu contraseña

	    public static void main(String[] args) {

	        Scanner sc = new Scanner(System.in);
	        int opcion;

	        do {
	            System.out.println("\n===== MENÚ CURSOS =====");
	            System.out.println("1. Insertar curso");
	            System.out.println("2. Mostrar cursos");
	            System.out.println("3. Buscar curso");
	            System.out.println("4. Actualizar curso");
	            System.out.println("5. Eliminar curso");
	            System.out.println("0. Salir");
	            System.out.print("Seleccione una opción: ");
	            opcion = sc.nextInt();
	            sc.nextLine(); // limpiar buffer

	            switch (opcion) {

	                case 1:
	                    insertarCurso(sc);
	                    break;

	                case 2:
	                    mostrarCursos();
	                    break;

	                case 3:
	                    buscarCurso(sc);
	                    break;

	                case 4:
	                    actualizarCurso(sc);
	                    break;

	                case 5:
	                    eliminarCurso(sc);
	                    break;

	                case 0:
	                    System.out.println("Saliendo del programa...");
	                    break;

	                default:
	                    System.out.println("Opción inválida.");
	            }

	        } while (opcion != 0);

	        sc.close();
	    }

	    // 1️⃣ INSERTAR
	    public static void insertarCurso(Scanner sc) {
	        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {

	            System.out.print("Nombre: ");
	            String nombre = sc.nextLine();

	            System.out.print("Profesor: ");
	            String profesor = sc.nextLine();

	            System.out.print("Horas: ");
	            int horas = sc.nextInt();
	            sc.nextLine();

	            String sql = "INSERT INTO cursos (nombre, profesor, horas) VALUES (?, ?, ?)";
	            PreparedStatement ps = conn.prepareStatement(sql);

	            ps.setString(1, nombre);
	            ps.setString(2, profesor);
	            ps.setInt(3, horas);

	            int filas = ps.executeUpdate();
	            System.out.println("Filas insertadas: " + filas);

	        } catch (SQLException e) {
	            e.printStackTrace();
	        }
	    }

	    // 2️⃣ MOSTRAR
	    public static void mostrarCursos() {
	        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {

	            String sql = "SELECT * FROM cursos";
	            PreparedStatement ps = conn.prepareStatement(sql);
	            ResultSet rs = ps.executeQuery();

	            while (rs.next()) {
	                System.out.println("ID: " + rs.getInt("id") +
	                                   " | Nombre: " + rs.getString("nombre") +
	                                   " | Profesor: " + rs.getString("profesor") +
	                                   " | Horas: " + rs.getInt("horas"));
	            }

	        } catch (SQLException e) {
	            e.printStackTrace();
	        }
	    }

	    // 3️⃣ BUSCAR
	    public static void buscarCurso(Scanner sc) {
	        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {

	            System.out.print("Ingrese nombre del curso: ");
	            String nombre = sc.nextLine();

	            String sql = "SELECT * FROM cursos WHERE nombre = ?";
	            PreparedStatement ps = conn.prepareStatement(sql);
	            ps.setString(1, nombre);

	            ResultSet rs = ps.executeQuery();

	            boolean encontrado = false;

	            while (rs.next()) {
	                encontrado = true;
	                System.out.println("ID: " + rs.getInt("id") +
	                                   " | Profesor: " + rs.getString("profesor") +
	                                   " | Horas: " + rs.getInt("horas"));
	            }

	            if (!encontrado) {
	                System.out.println("Curso no encontrado.");
	            }

	        } catch (SQLException e) {
	            e.printStackTrace();
	        }
	    }

	    // 4️⃣ ACTUALIZAR
	    public static void actualizarCurso(Scanner sc) {
	        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {

	            System.out.print("Ingrese ID del curso: ");
	            int id = sc.nextInt();

	            System.out.print("Nuevo número de horas: ");
	            int horas = sc.nextInt();
	            sc.nextLine();

	            String sql = "UPDATE cursos SET horas = ? WHERE id = ?";
	            PreparedStatement ps = conn.prepareStatement(sql);

	            ps.setInt(1, horas);
	            ps.setInt(2, id);

	            int filas = ps.executeUpdate();
	            System.out.println("Filas modificadas: " + filas);

	        } catch (SQLException e) {
	            e.printStackTrace();
	        }
	    }

	    // 5️⃣ ELIMINAR
	    public static void eliminarCurso(Scanner sc) {
	        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {

	            System.out.print("Ingrese ID del curso a eliminar: ");
	            int id = sc.nextInt();
	            sc.nextLine();

	            String sql = "DELETE FROM cursos WHERE id = ?";
	            PreparedStatement ps = conn.prepareStatement(sql);

	            ps.setInt(1, id);

	            int filas = ps.executeUpdate();
	            System.out.println("Filas eliminadas: " + filas);

	        } catch (SQLException e) {
	            e.printStackTrace();
	        }
	    }
	}

