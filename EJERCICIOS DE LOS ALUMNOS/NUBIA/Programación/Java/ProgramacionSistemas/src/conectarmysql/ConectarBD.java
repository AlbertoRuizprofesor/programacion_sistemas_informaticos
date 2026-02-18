package conectarmysql;

// importar herramientas
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;


public class ConectarBD {
	
		public static void main (String[] args) throws SQLException {
			// declaramos objetos necesarios:
			Connection conn=null;
			
		try {
			conn= DriverManager.getConnection("jdbc:mysql://localhost/phoneland_shop", "root","");
			
			if (conn != null) {
				System.out.println("La conexión a base de datos OK");
				conn.close();
			}
		}
		catch(SQLException e)
		{System.out.println("Error en la conexión "+e.getMessage());
	
		}
	}
}