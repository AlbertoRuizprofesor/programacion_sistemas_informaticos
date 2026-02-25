package preparedStatement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.PreparedStatement;



public class ConectaDB {





	public static void main(String[] args) throws SQLException{
		Connection conn=null;
		PreparedStatement pstmt=null;
		/*String sql="CREATE DATABASE if not exists empresa2";*/
	    /*String sql="CREATE TABLE clientes (id INT PRIMARY KEY,"
		      		+ "nif VARCHAR(10) NOT NULL,"
		      		+ "nombre VARCHAR(60) NOT NULL,"
		      		+ "edad VARCHAR(2))";*/
		 /*String sql="CREATE TABLE proveedores (id INT PRIMARY KEY,"
  		+ "nombre VARCHAR(60) NOT NULL,"
  		+ "telefono VARCHAR(9),"
  		+ "email VARCHAR(60))";*/
		/*String sql="CREATE TABLE productos (id INT PRIMARY KEY,"
  		+ "nombre VARCHAR(60) NOT NULL,"
  		+ "precio DECIMAL(10,2))";*/
		
		 /*String sql="INSERT INTO clientes(id,"+ "nif,nombre,edad)"+
					"VALUES (1,'11111','alberto','40')";*/
		/*String sql="INSERT INTO proveedores(id,telefono,nombre,email)"+
		"VALUES (1,'microsoft','357093','info@microsoft')";*/
		/*String sql="INSERT INTO productos(id,nombre,precio)"+
		"VALUES (1,'portatil','1500.00')";*/
		
		//String sql="SELECT * FROM clientes";
		String sql="SELECT * FROM productos";
		//String sql="SELECT * FROM proveedores";
		
		try {
			//desde aqui se carga el driver JDBC
			conn=DriverManager.getConnection("jdbc:mysql://localhost/empresa2"
					,"root","");
			
			pstmt=conn.prepareStatement(sql);
			pstmt.execute(sql);
			System.out.println("Creada la tabla");
			
			//MOSTRAR DATOS
			ResultSet rs=pstmt.executeQuery(sql);
			/*while(rs.next()) {
				int id=rs.getInt("id");
				String nif=rs.getString("nif");
				String nombre=rs.getString("nombre");
				String edad=rs.getString("edad");
				System.out.println("id: "+id+ ", nif : "+nif+ ", nombre : "+nombre+", edad : "+edad);
			};*/
			/*while(rs.next()) {
			    int id = rs.getInt("id");
			    String nombre = rs.getString("nombre");
			    String telefono = rs.getString("telefono");
			    String email = rs.getString("email");
			    System.out.println("id: " + id + ", nombre: " + nombre + ", telefono: " + telefono+",email: " +email);
			};*/
			while(rs.next()) {
			    int id = rs.getInt("id");
			    String nombre = rs.getString("nombre");
			    double precio = rs.getDouble("precio");
			    System.out.println("id: " + id + ", nombre: " + nombre + ", precio: " + precio);
			};
		
			conn.close();
			pstmt.close();
			
		}
		catch(SQLException e) {
			//System.out.println("error en la conexion "+e.getMessage());	
			e.printStackTrace();
		}
	}
}
