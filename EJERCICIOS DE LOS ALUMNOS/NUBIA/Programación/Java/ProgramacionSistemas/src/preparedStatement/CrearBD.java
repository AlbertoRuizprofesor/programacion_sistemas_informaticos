package preparedStatement;

// importar herramientas
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.Statement;

public class CrearBD {
	
			public static void main (String[] args) throws SQLException {
				// declaramos objetos necesarios:
				Connection conn=null;
				PreparedStatement stmt=null;
				String sql="CREATE DATABASE IF NOT EXISTS empresa2";
				
			try {
				conn= DriverManager.getConnection("jdbc:mysql://localhost/", "root","");
				stmt=conn.prepareStatement(sql);
				stmt.execute(sql);
				System.out.println("Base de datos 'empresa2' creada");
				conn.close();
				stmt.close();
			}
			catch(SQLException e)
			{System.out.println("Error en la conexión "+e.getMessage());
			
		
			}
		}
	}


