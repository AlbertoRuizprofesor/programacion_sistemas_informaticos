package conectarmysql;

// importar herramientas
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class CrearBD {
	
			public static void main (String[] args) throws SQLException {
				// declaramos objetos necesarios:
				Connection conn=null;
				Statement stmt=null;
				String sql="CREATE DATABASE IF NOT EXISTS empresa1";
				
			try {
				conn= DriverManager.getConnection("jdbc:mysql://localhost/", "root","");
				stmt=conn.createStatement();
				stmt.execute(sql);
				System.out.println("Base de datos 'empresa1' creada");
				conn.close();
				stmt.close();
			}
			catch(SQLException e)
			{System.out.println("Error en la conexión "+e.getMessage());
			
		
			}
		}
	}


