package conectarmysql;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class TablaProductos {
	public static void main (String[] args) throws SQLException {

/*
		// declaramos objetos necesarios:
		Connection conn=null;
		Statement stmt=null;
		String sql="CREATE TABLE IF NOT EXISTS productos (id INT PRIMARY KEY,"
				+ "nombre VARCHAR(60) NOT NULL,"
				+ "precio DECIMAL (10,2))";
		
	try {
		conn= DriverManager.getConnection("jdbc:mysql://localhost/empresa1", "root","");
		stmt=conn.createStatement();
		stmt.execute(sql);
		System.out.println("Tabla 'productos' creada");
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

*/
		// declaramos objetos necesarios:
		Connection conn=null;
		Statement stmt=null;
		String sql="INSERT INTO productos (id, "
				+ "nombre, precio)" +
				"VALUES (1, 'portátil', '1500.00')";
		
	try {
		conn= DriverManager.getConnection("jdbc:mysql://localhost/empresa1", "root","");
		stmt=conn.createStatement();
		stmt.executeUpdate(sql); //executeUpdate para actualizar tabla
		System.out.println("Datos insertados en 'clientes'");
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


