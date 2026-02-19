package conectar;

// importar herramientas
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class CrearBDAcademia {
	public static void main (String[] args) throws SQLException {
		// declaramos objetos necesarios:
		Connection conn=null;
		PreparedStatement stmt=null;
		String sql="CREATE DATABASE IF NOT EXISTS academia";
		
		try {
			conn= DriverManager.getConnection("jdbc:mysql://localhost/", "root","");
			stmt=conn.prepareStatement(sql);
			stmt.execute(sql);
			System.out.println("Base de datos 'academia' creada");
			
			conn.close();
			stmt.close();
		}
		catch(SQLException e)
		{System.out.println("Error en la conexión "+e.getMessage());
		}
	}
}




