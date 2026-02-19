package conectarmysql;

	import java.sql.Connection;
	import java.sql.DriverManager;
	import java.sql.SQLException;
	import java.sql.Statement;
	public class InsertarDatos {

		public static void main (String[] args) throws SQLException {
			// declaramos objetos necesarios:
			Connection conn=null;
			Statement stmt=null;
			String sql="INSERT INTO clientes (id, "
					+ "nif, nombre, edad)" +
					"VALUES (1,'00000000A', 'Nubia', '20')";
			
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

