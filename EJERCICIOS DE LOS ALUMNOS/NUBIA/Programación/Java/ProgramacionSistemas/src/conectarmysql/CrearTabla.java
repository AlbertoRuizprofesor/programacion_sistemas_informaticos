package conectarmysql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class CrearTabla {
	public static void main (String[] args) throws SQLException {
		// declaramos objetos necesarios:
		Connection conn=null;
		Statement stmt=null;
		String sql="CREATE TABLE IF NOT EXISTS proveedores (id INT PRIMARY KEY,"
				+ "nombre VARCHAR(60) NOT NULL,"
				+ "telefono VARCHAR(9),"
				+ "email VARCHAR(60))";
		
	try {
		conn= DriverManager.getConnection("jdbc:mysql://localhost/empresa1", "root","");
		stmt=conn.createStatement();
		stmt.execute(sql);
		System.out.println("Tabla 'proveedores' creada");
		conn.close();
		stmt.close();
	}
	catch(SQLException e)
	{e.printStackTrace();
	{System.out.println("Error en la conexión "+e.getMessage());	
	}

		}
	}
}
